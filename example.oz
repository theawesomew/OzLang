int fib int a: {
    if (a == 0) {
        return 1
    }

    if (a == 1) {
        return 1
    } else {
        return fib(a-1) + fib(a-2)
    }

    return 0
}

fib(10)