package com.mycompany.app;

import apidiff.*;
import apidiff.Change;
import apidiff.Result;
import apidiff.enums.Classifier;

public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        try{
            APIDiff diff = new APIDiff("airbnb/lottie-android", "https://github.com/airbnb/lottie-android.git");
            diff.setPath("executions/projects");
            
            Result result = diff.detectChangeAllHistory("master", Classifier.API);
           
            for(Change changeMethod : result.getChangeMethod()){
              
                System.out.println("\n" + changeMethod.getCategory().getDisplayName() + " - " + changeMethod.getDescription());
            }
        
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
