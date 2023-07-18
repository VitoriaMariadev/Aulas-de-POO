class PessoaTs {
    nome: string;
    idade: number;
    peso: number;
    altura: number;
  
    constructor(nome: string, idade: number, altura: number, peso: number) {
      this.nome = nome;
      this.idade = idade;
      this.altura = altura;
      this.peso = peso;
    }
  
    envelhecer(idade: number): void {
      try {
        if (idade <= 0) {
          console.log('Valor inválido');
          return;
        }
  
        this.idade += idade;
  
        if (this.idade < 21) {
          this.altura += idade * 0.005;
        }
      } catch (error) {
        console.log('Não foi possível realizar essa ação');
      }
    }
  
    engordar(peso: number): void {
      try {
        if (peso <= 0) {
          console.log('Valor inválido');
          return;
        }
  
        this.peso += peso;
      } catch (error) {
        console.log('Não foi possível realizar essa ação');
      }
    }
  
    emagrecer(peso: number): void {
      try {
        if (peso <= 0) {
          console.log('Valor inválido');
          return;
        }
  
        this.peso -= peso;
      } catch (error) {
        console.log('Não foi possível realizar essa ação');
      }
    }
  
    crescer(altura: number): void {
      try {
        if (altura <= 0) {
          console.log('Valor inválido');
          return;
        }
  
        this.altura += altura;
      } catch (error) {
        console.log('Não foi possível realizar essa ação');
      }
    }
  }
  
  const pessoa1Ts = new PessoaTs('Vitória', 16, 45, 1.60);
  
  pessoa1Ts.envelhecer(3);
  
  console.log(pessoa1Ts.idade);
  