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

    let numbers_replace = vec![
        ("zero"  , "zero0zero"),
        ("one"   , "one1one"),
        ("two"   , "two2two"),
        ("three" , "three3three"),
        ("four"  , "four4four"),
        ("five"  , "five5five"),
        ("six"   , "six6six"),
        ("seven" , "seven7seven"),
        ("eight" , "eight8eight"),
        ("nine"  , "nine9nine")
    ];
    
    let tall : i32 = input
        .split("\n")
        .map(|linje|
            numbers_replace
                .iter()
                .copied()
                .fold(linje.to_string(), |acc, (word, repl)| {
                    acc.replace(word, repl)
                })
        )
        .map(|linje|
            kombiner(
                første_siffer(&linje),
                siste_siffer(&linje)
            )
        )
        .sum();

    println!("{}", tall);
    // 54094

    Ok(())
}