def fun1():
    x = 5
    def fun2():
        y = 3
        def fun3():
            g = 7
            def fun4():
                nonlocal x
                x = "Слово"
                print(x)
            fun4()
        fun3()
    fun2()
fun1()