package com.madonahsyombua.ml;

import java.util.ArrayList;
import java.util.List;
import net.sf.classifier4J.ClassifierException;
import net.sf.classifier4J.vector.HashMapTermVectorStorage;
import net.sf.classifier4J.vector.TermVectorStorage;
import net.sf.classifier4J.vector.VectorClassifier;

public class SimpleNameSearch {

	public SimpleNameSearch() {
		//welcome new team members feel free to add some methods here
		List<String> name = new ArrayList<>();
		
		name.add("madonah");
		name.add("madona");
		name.add("madonna");
		name.add("maddona");
		name.add("maddoonna");
		name.add("madonahhh");
		name.add("madonayyy");
		name.add("madonnauuu");
		name.add("maddonattt");
		name.add("maddoonnaiii");
		
		
		TermVectorStorage storage = new HashMapTermVectorStorage();
		VectorClassifier vc = new VectorClassifier(storage);
		//correct string name when you enter search"
		String correctName = "madonah";
		
		for(String names: name) {
			try {
				
				vc.teachMatch("sterm",correctName);
				
				double results = vc.classify("sterm", names);
			
				System.out.println(names + " = " + results);
				
				
			}catch(ClassifierException e) {
				
				e.printStackTrace();
			}
			
		}
		
	}
	

	public static void main(String[] args) {
		
		SimpleNameSearch ns = new SimpleNameSearch();
		
	}
	
}
