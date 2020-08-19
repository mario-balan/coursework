public class Voo {
	
	private int codigo, cadeiras, cadeirasOcupadas;
	private Data data;
	
	public Voo (int codigo, Data data, int cadeiras){
		this.codigo = codigo;
		this.cadeiras = cadeiras;
		this.data = data;
	}
	
	public int getVoo(){
		return codigo;
	}
	
	public boolean verifica(int numeroCadeira){
		if (numeroCadeira <= cadeirasOcupadas)
			return false;
		return true;
		
	}
	
	public int vagas(){
		return (cadeiras - cadeirasOcupadas);
	}
	
	public void setCadeirasOcupadas(int cadeirasOcupadas){
		this.cadeirasOcupadas = cadeirasOcupadas;
	}
	
	public boolean ocupa(int numeroCadeira) {
		if (numeroCadeira <= cadeirasOcupadas){
			return false;
		} else{
			cadeirasOcupadas = cadeirasOcupadas + 1;
			return true;
		}
	}
	
	public static void main(String[] args) {

		Voo voo01 = new Voo (123, new Data(11,03,2018), 100);
		voo01.setCadeirasOcupadas(60);
		
		System.out.println(voo01.getVoo() + " " + voo01.vagas() + " " + voo01.verifica(61));
		System.out.println(voo01.ocupa(81));
		System.out.println(voo01.getVoo() + " " + voo01.vagas() + " " + voo01.verifica(61));
	}

}
