if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "e", "f", "i"}
    b = {"a", "b", "k", "n"}
    c = {"e", "f", "n", "o", "w", "x"}
    d = {"a", "d", "e", "o", "p", "t", "u"}

    x = (a.union(b)).intersection(c)
    print(f"x = {x}")

    an = u.intersection(b)

    y = (an.intersection(b)).difference(c.union(d))
    print(f"y = {y}")
