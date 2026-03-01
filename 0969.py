build = [
        "Финансовый отчёт",
        "Доходы выросли на 20%",
        "Расходы сократились на 5%",
        "Прибыль составила 1.5 млн"
        ]
        
metas = dict(
            author="Иван",
            date="2026-02-28",
            version="1.0"
            )
            
            
def met(**meta):
    print("\nМетаданные")
    for k, v in meta.items():
        print(f"{k}: {v}")


def sec(title, *sections, **meta):
    x = "=" * 3
    print(f"{x}{title}{x}")
    counter = 1
    for i in range(len(sections)):
        print(f"{counter}. {sections[i]}")
        counter += 1
    met(**meta)
    

sec(*build, **metas)