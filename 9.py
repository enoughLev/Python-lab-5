def ask_password(login, password, success, failure):
    vowels = set("aeiouy")

    login = login.lower()
    password = password.lower()

    def split_chars(str):
        vow = [ch for ch in str if ch in vowels]
        con = [ch for ch in str if ch not in vowels]
        return vow, con

    login_vowels, login_consonants = split_chars(login)
    password_vowels, password_consonants = split_chars(password)

    vowels_correct = (len(password_vowels) == 3)
    consonants_correct = (password_consonants == login_consonants)

    if vowels_correct and consonants_correct:
        success(login)
    else:
        if not vowels_correct and not consonants_correct:
            error_msg = "Everything is wrong"
        elif not vowels_correct:
            error_msg = "Wrong number of vowels"
        else:
            error_msg = "Wrong consonants"
        failure(login, error_msg)


def main(login, password):
    def on_success(user):
        print(f"Привет, {user}!")

    def on_failure(user, error):
        print(f"Кто-то пытался притвориться пользователем {user}, но в пароле допустил ошибку: {error.upper()}.")

    ask_password(login, password, on_success, on_failure)


main("login", "aaalgn")
main("", "")
main("anaconda", "neconad")  # я чуть не умер от такого задания
