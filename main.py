import foo

from flask import Flask

app = Flask(__name__)  # экземпляр Flask


def main():
    @app.route("/")
    def read_candidates():
        """Выводим данные всех кандидатов """
        read_page = foo.load_page()

        return read_page

    @app.route("/candidates/<int:x>")
    def read_candidate(x):
        """Выводим 'img' и данные одного кандидата по id"""
        read_link = foo.get_img(x)

        return read_link

    @app.route("/skills/<x>")
    def read_candidate_skill(x):
        """Выводим кандидатов у которых есть 'skills'"""
        read_skill = foo.get_skill(x)

        return read_skill

    app.run()


if __name__ == '__main__':
    main()
