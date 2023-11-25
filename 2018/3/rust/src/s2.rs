use rust_helper::input_file;
use std::cmp;
use std::collections::{vec_deque, VecDeque};

fn split_line_by(string: &String, token: &str) -> Vec<String>
{
    let words : Vec<String> = string.split(token).map(|w| w.to_string()).collect();
    return words;
}

fn split_array_by(strings: &Vec<String>, token: &str) -> Vec<Vec<String>> {
    let mut result = Vec::new();

    for s in strings
    {
        //let words: Vec<String> = s.split(token).map(|w| w.to_string()).collect();
        let words = split_line_by(&s, token); 
        result.push(words);
    }

    return result;
}

mod rectangle{
    #[derive(Debug,Copy,Clone)] //makes a struct printable via {:?}
    pub struct Rectangle {
        pub x: i32,
        pub y: i32,
        pub w: i32,
        pub h: i32,
    }

    pub fn new(x: i32,y: i32,w: i32,h: i32) -> Rectangle
    {
        return Rectangle{x,y,w,h};   
    }

    pub fn get_overlap(r1 : &Rectangle,r2 : &Rectangle) -> (bool ,Rectangle)
    {
            let mut res : (bool,Rectangle) =(false,new(0,0,0,0));

            if r2.x < r1.x +r1.w &&
               r1.x < r2.x +r2.w &&
               r2.y < r1.y +r1.h &&
               r1.y < r2.y +r2.h
            {
                println!("collision!   \n  R1:  {:?},\n  R2:  {:?}",r1,r2  );
                let end_x = std::cmp::min(r2.x+ r2.w, r1.x+r1.w);  //width collision
                let end_y = std::cmp::min(r2.y+ r2.h, r1.y+r1.h);  //width collision

                let col_x = std::cmp::max(r2.x,r1.x);
                let col_y = std::cmp::max(r2.y,r1.y);

                //println!("  start:  {col_x} {col_y}");
                //println!("  end:    {end_x} {end_y}");
                //println!("  size:   {} {}",end_x-col_x,end_y-col_y);

                res.0= true;
                res.1= new(col_x, col_y,end_x-col_x,end_y-col_y );
                println!("  {:?}",res.1);
                // println!("  {:?}",coll_rect);
            }
            return res;
    }
}


pub fn run(  )
{
    println!("\n\np2!!");

    let input_text = rust_helper::read_lines(
        &rust_helper::input_file!(false));

    let splitted_lines = split_array_by(&input_text, " ");

    let mut rectangles : Vec<rectangle::Rectangle> = Vec::new(); 

    for rect_line in splitted_lines
    {
        println!("{:?}",rect_line);
        let mut base_split = split_line_by( rect_line.get(2).unwrap(),",");
        base_split[1]= split_line_by( base_split.get(1).unwrap(),":").join("");
        
        println!("{:?}",base_split);
        let pos =  rust_helper::int_list(base_split);

        println!("{:?}",pos);
        let size = rust_helper::int_list(split_line_by( rect_line.get(3).unwrap(),"x") ); //w,h format

        let rect = rectangle::new( *pos.get(0).unwrap(),*pos.get(1).unwrap(),*size.get(0).unwrap(),*size.get(1).unwrap() );
        println!("New rect {:?}",rect);

        rectangles.push(rect);
    }


    println!("done setting up rects ...");
    let mut check_list = VecDeque::from(rectangles.clone());

    for rect in rectangles.iter().enumerate()
    {
        println!("  {}",rect.0);
        let mut overlaps = 0;

        
        
        for check_rect in check_list.iter().enumerate()
        {
            if check_rect.0 == rect.0
            {
                continue;
            }

            let overlap = rectangle::get_overlap(rect.1, &check_rect.1);
            if overlap.0 == true
            {
                overlaps +=1;
            }
        }

        if overlaps == 0
        {
            println!("Found no collision rect!!! ID: {}",rect.0 + 1);
            break;
        }
    }
}
