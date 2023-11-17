
//use std::io;
use std::fs::File;
use std::io::{BufReader, BufRead};
use std::vec;




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
