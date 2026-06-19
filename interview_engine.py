class InterviewEngine:

    def __init__(self):

        self.easy_questions = [

            {
                "question":
                "What is Python?",

                "keywords":
                [
                    "programming",
                    "language"
                ]
            },

            {
                "question":
                "What is a list in Python?",

                "keywords":
                [
                    "collection",
                    "ordered"
                ]
            }

        ]

        self.medium_questions = [

            {
                "question":
                "Explain OOP concepts.",

                "keywords":
                [
                    "inheritance",
                    "polymorphism",
                    "encapsulation"
                ]
            },

            {
                "question":
                "What is REST API?",

                "keywords":
                [
                    "http",
                    "api",
                    "client"
                ]
            }

        ]

        self.hard_questions = [

            {
                "question":
                "Explain multithreading in Python.",

                "keywords":
                [
                    "thread",
                    "concurrency",
                    "parallel"
                ]
            },

            {
                "question":
                "How does JWT authentication work?",

                "keywords":
                [
                    "token",
                    "authentication",
                    "payload"
                ]
            }

        ]

        self.score = 0

    def evaluate_answer(

        self,
        answer,
        keywords

    ):

        answer = answer.lower()

        matches = 0

        for keyword in keywords:

            if keyword in answer:

                matches += 1

        return matches

    def run_level(

        self,
        questions,
        level

    ):

        print(
            f"\n===== {level} LEVEL ====="
        )

        for item in questions:

            print(
                "\nQuestion:"
            )

            print(
                item["question"]
            )

            answer = input(
                "\nYour Answer:\n"
            )

            score = self.evaluate_answer(

                answer,

                item["keywords"]

            )

            self.score += score

            print(
                f"\nPoints Earned: "
                f"{score}"
            )

    def start(self):

        self.run_level(

            self.easy_questions,

            "EASY"

        )

        if self.score >= 2:

            self.run_level(

                self.medium_questions,

                "MEDIUM"

            )

        if self.score >= 5:

            self.run_level(

                self.hard_questions,

                "HARD"

            )

        print(
            "\n===================="
        )

        print(
            "INTERVIEW FINISHED"
        )

        print(
            "===================="
        )

        print(
            f"\nFinal Score: "
            f"{self.score}"
        )