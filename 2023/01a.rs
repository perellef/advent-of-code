// løst

use std::fs;
use std::io;

fn første_siffer(s: &str) -> char {
    s.chars()
        .find(|c| c.is_numeric())
        .unwrap()
}

fn siste_siffer(s: &str) -> char {
    s.chars()
        .rev()
        .find(|c| c.is_numeric())
        .unwrap()
}

fn kombiner(c1: char, c2: char) -> i32 {
    format!("{}{}", c1, c2).parse::<i32>().unwrap()
}

fn main() -> io::Result<()> {
    let input : String = fs::read_to_string("01.txt")?;
    
    let tall : i32 = input
        .split("\n")
        .map(|linje| kombiner(
                første_siffer(linje),
                siste_siffer(linje)
            )
        )
        .sum();

    println!("{}", tall);
    // 54968

    Ok(())
}