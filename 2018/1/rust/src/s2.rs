
use std::collections::HashMap;
//use std::io;
use std::fs::File;
use std::hash::Hash;
use std::io::{BufReader, BufRead};
use std::iter::{MapWhile, FlatMap};
use std::vec;




fn read_lines(file_name: &str) -> Vec<String> {
    let mut str_list : Vec<String> = vec::Vec::new();

    let file_ = File::open(file_name).expect("file not found!");
    let reader = BufReader::new(file_);
    
    for line in reader.lines()
    {
        str_list.push( line.unwrap());
    }
    return str_list;
}

//convert a list of strings into 
fn int_list ( str_list : Vec<String>) -> Vec<i32>
{
    let mut int_list: Vec<i32> = Vec::new();

    for str_num in str_list.iter()
    {
        int_list.push(str_num.trim().parse().unwrap());
    }

    return int_list;
}


pub fn run(  )
{
    println!("----------------------");
    println!("P2");
    let txt_lines = read_lines("src/input.txt");
    let mut numbers = int_list(txt_lines);
    let mut dupe_map: HashMap<i32,bool> = HashMap::new();
    let mut value = 0;
    let mut found_dupe = false;

    //numbers = vec![1,-1];
    
    while found_dupe!= true
    {
        println!("run...");

        for num in numbers.iter()
        {
            
            dupe_map.insert(value,true);

            //println!("{}",num);
            value+= num;

            if  dupe_map.contains_key(&value) == true
            {
                println!("Found value {} twice",value);
                found_dupe = true;
                break
            }
            else
            {
                //println!("Searched {value}");
                // for item in dupe_list.iter()
                //     {
                //         println!("   {}",item);
                //     }
            }

        }
    }
    //println!("End val {}", value);

}
