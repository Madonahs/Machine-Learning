library(quantmod)
library(downloader)
library(e1071)
library(neuralnet)

window = 10

#Data shared with teams

sp500 <- new.env()

getSymbols("^GSPC", env = sp500, src = "yahoo", from = "1930-01-04", to = Sys.Date())

GSPC <- sp500$GSPC
dim(GSPC)
names(GSPC)
head(GSPC)
names(GSPC) <- c("Open","High","Low","Close","Volume","Adjusted")
head(GSPC)

GSPC1 <- as.data.frame(array(0,dim=c(dim(GSPC)[1], dim(GSPC)[2]+1)) )
names(GSPC1) = c("time",colnames(GSPC))
GSPC1[,1] <- index(GSPC)
GSPC1[,c(2:dim(GSPC1)[2])] = GSPC

dim(GSPC1)
names(GSPC1)
head(GSPC1)
apply(GSPC1,2,function(x) sum(is.na(x)))

SPX <- GSPC1[,c(1,5)]
head(SPX)
apply(SPX,2,function(x) sum(is.na(x)))
#SPX <- SPX[!is.na(SPX)]


dim(SPX)
data <- as.data.frame(array(0,dim=c(dim(SPX)[1]-window, window)) )

dim(data)

names(data) 


k = 1# window
j = 1

for(k in window:dim(data)[1])
{ 
  for(j in 1:window)
  {
    data[k,j] = SPX[k+j,2]
  }
  
}

data_O <- as.data.frame(array(0,dim = c(dim(data)[1],dim(data)[2]+1)))
data_O[,c(2:dim(data_O)[2])] = data
data_O[,1] = SPX[-c(1:window),1]
dim(data_O)
#names(data_O) = names(data)
names(data_O)
head(data_O)
data_O[(dim(data_O)[1]-10):dim(data_O)[1],]
SPX[(dim(SPX)[1]-50):dim(SPX)[1],2]
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
my_Y = paste("V",window+1,sep = "")

#+++++++++++++++++++ FORECASTING +++++++++++++++++++++++++++++

data_O[-c(1:2*window),]
dim(data_O)
head(data_O)
names(data_O) # = c()
nrow(data_O)
horizon1 = 16990 #1328 #1324
horizon2 = 17003 #1332 #1328
leng = 40
start = horizon1 - leng #1200 #1204

nr = ncol(data_O)
data1 = data_O[c(start:horizon1),c(1:nr)]
str(data1)
dim(data1)
names(data1)
data1[1:5,]
data1[dim(data1)[1],]
l1 = dim(data1)[1]
data1[l1-1,]
data1[l1,]
data1[l1+1,]
t = data1[,1]
y = data1[,nr]
#data <- data.frame(data1[,-c(1:2)])
data <- data.frame(data1[,-1])
names(data)
dim(data)


data2 = data_O[c(start:horizon2),c(1:nr)]
dim(data2)
l2 = dim(data2)[1]
#X2 = data2[c((l1+1):l2),-c(1,2,8)]
X2 = data2[c((l1+1):l2),-c(1,nr)]
newdata = data.frame(X2)
names(newdata)
dim(newdata)
newdata[1,]
newdata[dim(newdata)[1],]
d <- as.data.frame(array(NA,dim=c(l2-l1,dim(newdata)[2])) )
dim(d)
names(d) <- names(newdata)
newdata.SVR <- d
newdata.ANN <- d
newdata.LM <- d

#plot(t,y, xlab = "Dates", ylab = "Close",type = "l", col = "red", main = "NDX")

# Create a linear regression model
library(neuralnet)
apply(data,2,function(x) sum(is.na(x)))
maxs <- apply(data, 2, max) 
mins <- apply(data, 2, min)
scaled <- as.data.frame(scale(data, center = mins, scale = maxs - mins))
dim(scaled)
#model.lm <- lm(X_5 ~ ., scaled)
model.lm <- lm(V11 ~ ., scaled)
summary(model.lm)
predicted.lm <- predict(model.lm, scaled)
#lines(t, predicted.lm*(max(data$V11)-min(data$V11))+min(data$V11),type = "l", col = "black")

rmse <- function(error)
{
  sqrt(mean(error^2))
}
Max_abs_err <- function(error)
{
  max(abs(error))
}

error <- model.lm$residuals  
predictionRMSE <- rmse(error)  
predictionMax_abs_err <- Max_abs_err(error)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Let's fit the net:
library(neuralnet)
apply(data,2,function(x) sum(is.na(x)))
maxs <- apply(data, 2, max) 
mins <- apply(data, 2, min)
scaled <- as.data.frame(scale(data, center = mins, scale = maxs - mins))
dim(scaled)
#scaled = data
n <- names(data)
f <- as.formula(paste("V11 ~", paste(n[!n %in% "V11"], collapse = " + ")))
model.nn <- neuralnet(f,data= scaled,hidden=c(3,4,3),linear.output=T)
#plot(model.nn)
predict.nn <- compute(model.nn,scaled[,-6])

pr.nn_ <- predict.nn$net.result*(max(data$V11)-min(data$V11))+min(data$V11)
test.r <- (data$V11)
MSE.nn <- sum((test.r - pr.nn_)^2)/nrow(data)
rMSE.nn <- sqrt(MSE.nn)
#lines(t, pr.nn_,type = "l", col = "cyan")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#install.packages("e1071")
library(e1071)
model.untunedSVR <- svm(V11 ~ . ,kernel = "radial", gamma = 2, data)
model.untunedSVR$rho
model.untunedSVR$epsilon
model.untunedSVR$cost
model.untunedSVR$gamma

predicted.untunedSVR <- predict(model.untunedSVR, data)
lines(t, predicted.untunedSVR,type = "l", col = "blue")
error <- y - predicted.untunedSVR
svrPredictionRMSE <- rmse(error) 
svrPredictionMax_abs_err <- Max_abs_err(error) 


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
train <- scaled #data #data[index,]
tuneResult <- tune(svm, V11 ~ .,kernel = "radial",  data = train,
                   ranges = list(epsilon = seq(0,0.08,0.01), cost = seq(0.1,200,50),gamma = seq(0.1,200,50)) )
tunedModel <- tuneResult$best.model
E = tunedModel$epsilon
C = tunedModel$cost   
G = tunedModel$gamma

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
modelcross <- svm(V11 ~ .,kernel = "radial",epsilon = E, cost = C , gamma = G, data=scaled)
predicted.tunedSVR <- predict(modelcross, scaled)
#lines(t, predicted.tunedSVR*(max(data$V11)-min(data$V11))+min(data$V11),type = "l", col = "green")

#legend('topleft',c('data','OLS regression','aNN','untuned SVR','tuned SVR'),fill = c("red","black","cyan","blue","green"),  bty = 'n', border = NA)


tunedModelY <- predict(modelcross,scaled) 
error <- y - ( tunedModelY*(max(data$V11)-min(data$V11))+min(data$V11)  )
Tuned_svrPredictionRMSE <- rmse(error) 
Tuned_svrPredictionMax_abs_err <- Max_abs_err(error)


newdata.SVR[1,] = scaled[(l1),-1]
newdata.ANN[1,] = scaled[(l1),-1]
newdata.LM[1,] = scaled[(l1),-1]

firstwindow.SVR <- newdata.SVR[1,] 
firstwindow.ANN <- newdata.ANN[1,]
firstwindow.LM <- newdata.LM[1,]

p.SVR <- rep(0, dim(newdata)[1])
p.ANN <- rep(0, dim(newdata)[1])
p.LM <- rep(0, dim(newdata)[1])

firstwindow.SVR[2:(window-1)]
firstwindow.ANN[2:(window-1)]
firstwindow.LM[2:(window-1)]

p.SVR[1] <- predict(modelcross, newdata.SVR[1,])*(max(data$V11)-min(data$V11))+min(data$V11)
p.ANN[1] <- compute(model.nn, newdata.ANN[1,])$net.result*(max(data$V11)-min(data$V11))+min(data$V11)
p.LM[1] <- predict(model.lm, newdata.LM[1,])*(max(data$V11)-min(data$V11))+min(data$V11)

for(j in 2:dim(newdata)[1]) # (window)) #dim(newdata)[1])
{ # j=3
  newdata.SVR[j,] = cbind (firstwindow.SVR[2:(window-1)],p.SVR[j-1] )
  newdata.ANN[j,] = cbind (firstwindow.ANN[2:(window-1)],p.ANN[j-1] )
  newdata.LM[j,] = cbind (firstwindow.LM[2:(window-1)],p.LM[j-1] )
  
  p.SVR[j] <- predict(modelcross, newdata.SVR[j,])*(max(data$V11)-min(data$V11))+min(data$V11)
  p.ANN[j] <- compute(model.nn, newdata.ANN[j,])$net.result*(max(data$V11)-min(data$V11))+min(data$V11)
  p.LM[j] <- predict(model.lm, newdata.LM[j,])#*(max(data$X5)-min(data$X5))+min(data$X5)
  
  firstwindow.SVR <-  newdata.SVR[j,] 
  firstwindow.ANN <-  newdata.ANN[j,]
  firstwindow.LM <-  newdata.LM[j,]
  
}


final.output <- as.data.frame(array(NA,dim=c(8,dim(newdata)[1])) )
rownames(final.output) <- c("Date","True Price","SVR Price","ANN Price","LM price","True-SVR","True-ANN","True-LM")
final.output[1,] <- data2[c((l1+1):(l2)),1]
final.output[2,] <- data2[c((l1+1):(l2)),8]
final.output[3,] <- p.SVR
final.output[4,] <- p.ANN
final.output[5,] <- p.LM
final.output[6,]<- final.output[2,] - final.output[3,]
final.output[7,]<- final.output[2,] - final.output[4,]
final.output[8,]<- final.output[2,] - final.output[5,]

final.output