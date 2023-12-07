use rust_helper::input_file;

pub fn run(  )
{
    println!("\np2");
    let mut sum = 0;
    let input_text = rust_helper::read_lines(
        &rust_helper::input_file!(true));

    let num_list: Vec<&str>= [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine" ].to_vec();

    for mut line in input_text
    {

        println!("POST: {}",line);
        let mut num_list: Vec<char> = Vec::new();

        let mut num_part = "".to_string();
        let mut pos_nums = 
        for letter in line.chars()
        {
            if letter.is_ascii_digit()
            {
                num_list.push(letter);
            }
            else
            {
                
            }
        }
        
        let mut num_part: String= String::from("");
        num_part.push(num_list[0]);
        num_part.push(num_list[num_list.len()-1]);

        let num : i32 = num_part.parse().unwrap();
        println!("rnum {}",num);
        sum+= num;
    }
    println!("SUM: {}",sum);
}
