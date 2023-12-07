
//use std::io;
use std::fs::File;
use std::io::{BufReader, BufRead};
use std::vec;

// A samll helper for getting the wanted input file sample or real
pub fn input_file(use_sample: bool) -> String
{
    if use_sample == true
    {
        return "src/sample_input.txt".to_string();
    }
    else
    {
        return "src/input.txt".to_string();
    }
}

#[macro_export]
macro_rules! input_file {
    ($a: expr) => {
        input_file($a)
    };
    () => {
        input_file(false)
    };
}


//---------------
// split helpers:

pub fn split_line_by(string: &String, token: &str) -> Vec<String>
{
    let words : Vec<String> = string.split(token).map(|w| w.to_string()).collect();
    return words;
}

pub fn split_array_by(strings: &Vec<String>, token: &str) -> Vec<Vec<String>> {
    let mut result = Vec::new();

    for s in strings
    {
        //let words: Vec<String> = s.split(token).map(|w| w.to_string()).collect();
        let words = split_line_by(&s, token); 
        result.push(words);
    }

    return result;
}


//--------------

//base reader helper to get a array of lines
pub fn read_lines(file_name: &str) -> Vec<String> {
    let mut str_list : Vec<String> = vec::Vec::new();

    let file_ = File::open(file_name).expect("file not found!");
    let reader = BufReader::new(file_);
    
    for line in reader.lines()
    {
        str_list.push( line.unwrap());
    }
    return str_list;
}

//helper for converting a string list into a list of integers
pub fn int_list ( str_list : Vec<String>) -> Vec<i32>
{
    let mut int_list: Vec<i32> = Vec::new();

    for str_num in str_list.iter()
    {
        int_list.push(str_num.trim().parse().unwrap());
    }

    return int_list;
}

//#[cfg(test)]
//mod tests {
//    use super::*;
//
//    #[test]
//    fn it_works() {
//        let result = add(2, 2);
//        assert_eq!(result, 4);
//    }
//}
