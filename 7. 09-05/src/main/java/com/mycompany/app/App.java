package com.mycompany.app;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Hashtable;

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
            
            Hashtable<String,Integer> classBreakChanges  = new Hashtable<String,Integer>();
            Hashtable<String,Integer> classChanged  = new Hashtable<String,Integer>();

            for(Change changeType : result.getChangeType()){
                if(changeType.isBreakingChange()){
                    String bc = changeType.getCategory().getDisplayName();
                    if(classBreakChanges.containsKey(bc)){
                        classBreakChanges.replace(bc, classBreakChanges.get(bc) + 1);
                    }else{
                        classBreakChanges.put(bc, 1);
                    }

                    String cc = changeType.getElement();
                    if(classChanged.containsKey(cc)){
                        classChanged.replace(cc, classChanged.get(cc) + 1);
                    }else{
                        classChanged.put(cc, 1);
                    }   
                }
            }

            Hashtable<String,Integer> methodBreakChanges  = new Hashtable<String,Integer>();
            Hashtable<String,Integer> methodChanged  = new Hashtable<String,Integer>();

            for(Change changeMethod : result.getChangeMethod()){
                if(changeMethod.isBreakingChange()){
                    String bc = changeMethod.getCategory().getDisplayName();
                    if(methodBreakChanges.containsKey(bc)){
                        methodBreakChanges.replace(bc, methodBreakChanges.get(bc) + 1);
                    }else{
                        methodBreakChanges.put(bc, 1);
                    }

                    String cc = changeMethod.getElement();
                    if(methodChanged.containsKey(cc)){
                        methodChanged.replace(cc, methodChanged.get(cc) + 1);
                    }else{
                        methodChanged.put(cc, 1);
                    }   
                }
            }

            System.out.println("Quebras em classe:");
            maxValue(classBreakChanges);

            System.out.println("Classes com mais quebra:");
            maxValue(classChanged);

            System.out.println("Quebras em metodos:");
            maxValue(methodBreakChanges);

            System.out.println("Metodos com mais quebras:");
            maxValue(methodChanged);
            
        } catch (Exception e) {
            System.out.println(e.getMessage());
            System.out.println(e.getCause().getMessage());
            e.printStackTrace();
            
        }
    }

    
    public static void maxValue(Hashtable<String,Integer> h){
        ArrayList<KeyValuePar> a = new ArrayList<KeyValuePar>();
        for (String key : h.keySet()) {
            a.add(new KeyValuePar(key,h.get(key)));
        }
        if(a.size() > 0) {
            a.sort(
                new Comparator<KeyValuePar>(){
                    @Override
                    public int compare(KeyValuePar kva, KeyValuePar kvb){
                        return kva.value > kvb.value ? 1  : -1;
                    }
                }
            );

            int i = 0;
            for (KeyValuePar k : a) {
                System.out.println(k.key +": "+ k.value.toString() );
                i++;
                if(i==5)break;
            }
        }

    }
}

class KeyValuePar {
    String key;
    Integer value;
    public KeyValuePar(String key,Integer value){
        this.key = key;
        this.value = value;
    }
}