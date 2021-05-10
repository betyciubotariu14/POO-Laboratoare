class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "1.Procedeele specifice metodei contabilității sunt:\na) documentarea, evaluarea, circulatia si inventarierea;\nb) bilantul contabil, contul, balanta de verificare;\nc) inventarierea, contul, balanta de verificare;\nRaspuns:",
    "2.Care ecuație bilanțieră corespunde acelei reguli de funcționare a conturilor, cu privire la înregistrarea majorărilor elementelor bilanțiere?\na)A+x-x=P;\nb)A=P+x-x;\nc)A+x=P+x;\nRaspuns:",
    "3.Conform normelor legale din țara noastră principalele registre de contabilitate obligatorii sunt:\na) Registrul-jurnal, Registrul-inventar, Cartea-mare;\nb)Registrul-jurnal, Registrul-inventar,Registrul de incasari si plati;\nc)Registrul-jurnal, Registrul-inventar,Registrul de evidenta al salariilor;\nRaspuns:",
    "4.Analiza contabilă se efectuează:\na)dupa inregistrarea operatiilor in conturi, pentru verificarea acestora;\nb)inainte de inregistrarea operatiilor in conturi, in scopul stabilirii corecte a conturilor in care se inregistreaza;\nc)inainte ca operatiile economice sa fie consemnate in documente;\nRaspuns:",
    "5.A debita un cont înseamnă:\na)a inscrie o suma in partea stanga a contului;\nb)a inregistra operatii de majorare a conturilor de activ;\nc)a inregistra operatii de micsorare a activelor;\nRaspuns:",
    "6.După felul conturilor pe care le cuprind, balanțele de verificare sunt:\na)balante de verificare ordinare si extraordinare;\nb)balante de verificare totale si partiale;\ncbalante de verificare sintetice si analitice);\nRaspuns:",
    "7.Una dintre egalitățile specifice balanțelor de verificare sintetice este:\na)egalitatea intre totalul incasarilor si totalul platilor;\nb)egalitatea intre suma rulajelor debitoare si suma rulajelor creditoare;\nc)egalitatea inre conturile de cheltuieli si cele de venituri;\nRaspuns:",
    "8.Care din următoarele afirmații este adevărată?\na)balantele de verificare sunt operatii premergatoare intocmirii bilantului;\nb)balantele de verificare se intocmesc concomitent cu bilantul;\nc)balantele de verificare sunt operatii ulterioare intocmirii bilantului;\nRaspuns:",
    "9.Pregătirea inventarierii necesită:\na)bintocmirea unor masuri cu caracter organizatoric si contabil);\nb)intocmirea corecta a documentelor de gestiune;\nc)intocmirea contului de profit si pierdere;\nRaspuns:",
    "10.Operația de inventariere se realizează:\na)numai in prezenta unui expert contabil sau contabil autorizat;\nb)in prezenta a cel putin doua persoane;\nc)in prezenta tuturor membrilor comisiei si a gestionarului;\nRaspuns:",


]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "c"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Punctajul obtinut este", score)
run_quiz(questions)