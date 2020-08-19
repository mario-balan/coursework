public class Aluno{
	
	public static int contador = 1;
	
	private int matricula;
	private String nome;
	private float primeiraNota, segundaNota, trabalhoNota;
	
	public Aluno(String nome, float primeiraNota, float segundaNota, float trabalhoNota){
		matricula = contador++;
		this.nome = nome;
		this.primeiraNota = primeiraNota;
		this.segundaNota = segundaNota;
		this.trabalhoNota = trabalhoNota;
	}
		
	public int getMatricula(){
		return matricula;
	}
	
	public String getNome(){
		return nome;
	}
	
	public float calculaMedia(){
		return (primeiraNota * 2.5f + segundaNota * 2.5f + trabalhoNota * 2f ) / 7;
	}
	
	public float calculaExame(){
		float exame;
		exame = 10f - calculaMedia();
		if (exame <= 5){
			return 0;
		}
		else {
			return exame;			
		}
	}
	
	
	
	
	public static void main(String[] args) {

	Aluno aluno01 = new Aluno("Mario", 3.0f, 4.0f, 5.0f);
	Aluno aluno02 = new Aluno("Jarbas", 5.0f, 0.0f, 9.0f);
	Aluno aluno03 = new Aluno("Astolfo", 10.0f, 10.0f, 10.0f);
	
	System.out.println("ALUNO #" + aluno01.getMatricula() 
			+ "\nNome: " + aluno01.getNome() 
			+ "\nMédia: " + aluno01.calculaMedia() 
			+ "\nNota Mínima no Exame: " + aluno01.calculaExame()+ "\n");

	System.out.println("ALUNO #" + aluno02.getMatricula() 
			+ "\nNome: " + aluno02.getNome() 
			+ "\nMédia: " + aluno02.calculaMedia() 
			+ "\nNota Mínima no Exame: " + aluno02.calculaExame()+ "\n");
	
	System.out.println("ALUNO #" + aluno03.getMatricula() 
			+ "\nNome: " + aluno03.getNome() 
			+ "\nMédia: " + aluno03.calculaMedia() 
			+ "\nNota Mínima no Exame: " + aluno03.calculaExame()+ "\n");
	}

}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
/*	media() {
		
	}
	
	final(){
		
	}*/

