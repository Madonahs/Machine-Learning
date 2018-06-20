package com.madonahsyombua.ml;

import java.util.ArrayList;
import java.util.List;

import net.sf.classifier4J.ClassifierException;
import net.sf.classifier4J.vector.HashMapTermVectorStorage;
import net.sf.classifier4J.vector.TermVectorStorage;
import net.sf.classifier4J.vector.VectorClassifier;

public class SimpleNameSearch {

    public static void parametrizedSimpleSearch(List<String> searchList, String wordToSearch) {

        TermVectorStorage storage = new HashMapTermVectorStorage();
        VectorClassifier vc = new VectorClassifier(storage);

        for (String element : searchList) {
            try {

                vc.teachMatch("sterm", wordToSearch);

                double results = vc.classify("sterm", element);

                System.out.println(element + " = " + results);

            } catch (ClassifierException e) {

                e.printStackTrace();
            }

        }
    }

    public static void main(String[] args) {

        SimpleNameSearch ns = new SimpleNameSearch();
        System.out.println("Machine Learning: ");
        System.out.println("************************************");
        List<String> names = new ArrayList<String>();

        names.add("nida");
        names.add("nidu");
        names.add("nidha");
        names.add("rhizlane");
        names.add("niiddaa");
        names.add("needa");
        names.add("madonah");
        names.add("nidaa");
        names.add("madonnaah");
        names.add("chaiimaee");
        names.add("chaimae");
        System.out.println();
     
        parametrizedSimpleSearch(names,"nida");

        System.out.println("******************************************");
        parametrizedSimpleSearch(names,"madonah");

        System.out.println("******************************************");
        parametrizedSimpleSearch(names,"rhizlane");
        
         System.out.println("******************************************");
        parametrizedSimpleSearch(names,"chaimae");
        

    }

}
