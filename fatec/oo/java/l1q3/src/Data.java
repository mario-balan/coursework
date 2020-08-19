
public class Data {

	private int dia, mes, ano;
	
	public Data(int dia, int mes, int ano){
		// Por questões de simplificação, assumindo que todos os meses têm no máximo 31 dias e todos os anos têm 12 meses:
		if ((dia < 0 || dia > 31) || (mes < 1 || mes > 12)){
			this.dia = 01;
			this.mes = 01;
			this.ano = 0001;	
		}
		else{
			this.dia = dia;
			this.mes = mes;
			this.ano = ano;			
		}
	}
	
	public int getDia(){
		return dia;
	}
	
	public int getMes(){
		return mes;
	}	

	public int getAno(){
		return ano;
	}
	
	public String getMesExtenso(){
		String[] nomeMes = {"janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"};
		return nomeMes[mes - 1];
	}
	
	public int compara(int novoDia, int novoMes, int novoAno){
		int avgData01 = this.getAno() * 365 + this.getMes() * 30 + this.getDia();
		int avgData02 = novoAno * 365 + novoMes * 30 + novoDia;

		if (avgData01 < avgData02){
			return 1;
		}
		else if (avgData01 > avgData02){
			return -1;
		}
		else{
			return 0;
		}
	}


	public Data clona(){
		Data copiaData = new Data(this.getDia(), this.getMes(), this.getAno());
		return copiaData;
	}
    
    public boolean isBissexto() {
        if((ano % 4 == 0 || ano % 400 == 0) && ano % 100 != 0){
            return true;
        }
        else{
        	return false;
        }
    }
}