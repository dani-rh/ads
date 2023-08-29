agenda = {"Maria": "(41) 98765-4321", "João": "(11) 12345-6789"}
print(agenda.pop("Maria", "Contato com nome Maria localizado"))
print(agenda.pop("José", "Contato com nome José não localizado"))
print(agenda)