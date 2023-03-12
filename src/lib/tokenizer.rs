enum TokenType {
    IF,
    ELSE,
    RETURN,
    OPERATOR,
    TYPE,
    IDENTIFIER,
    STRING,
    NUMBER,
    COMMA,
    ASSIGNMENT,
    OPARENTHESIS,
    CPARENTHESIS,
    OBRACKET,
    CBRACKET,
}

struct Token {
    kind: TokenType,
    value: String,
}

fn tokenize (f: std::io::Result<std::fs::File>) -> Vec<Token> {
    let mut string = String::new();
    f.read_to_string(&mut string);

    string.retain(|c| !c.is_whitespace());

    let set = regex::RegexSet::new(&[
        r"if",
        r"else",
        r"return",
        r"(+|-|/|*|==|<|>|!=|<=|>=)",
        r"string|int",
        r"[a-zA-Z_]+",
        r"\".*?\"",
        r"\-?[0-9]+",
    ]).unwrap();

    let matches: Vec<_> = set.matches(string).into_iter();

    for m in matches {
        println!("Match: {}", m);
    }

    return Vec::new();
}
