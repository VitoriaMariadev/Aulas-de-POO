class Pessoa{
    constructor(nome, idade, altura, peso){
        this.nome = nome
        this.idade = idade
        this.altura = altura
        this.peso = peso
    }

    envelhecer(idade){
        try {
            if(idade <= 0){
                console.log('Valor inválido')
            }

            this.idade += idade

            if (this.idade >= 21){
                this.altura += (idade*0.005)
                
            }
        } catch (erro) {
            console.log('Não foi possível realizar a ação')
        }
    }

    engordar(peso){
        try {

            if (peso <= 0){
                console.log('Valor inválido')
            }

            this.peso += peso
            
        } catch (error) {
            console.log('Não foi possível realizar a ação')
        }
    }

    emagrecer(peso){
        try {

            if (peso <= 0){
                console.log('Valor inválido')
            }

            this.peso -= peso
            
        } catch (error) {
            console.log('Não foi possível realizar a ação')
        }
    }

    crescer(altura){
        try {

            if (altura <= 0){
                console.log('Valor inválido')
            }

            this.altura += altura
            
        } catch (error) {
            console.log('Não foi possível realizar a ação')
        }
    }

}

let pessoa1 = new Pessoa('Vitória', 21, 1.60, 45)

console.log(pessoa1.idade)

pessoa1.envelhecer(4)

console.log(pessoa1.idade)
