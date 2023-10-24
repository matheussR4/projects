/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package interfaceDados;

import Classes.Fornecedor;
import java.util.ArrayList;

/**
 *
 * @author Petheus Rodrigues
 */
public interface IFornecedor {
    public abstract boolean adicionarFornecedor(Fornecedor fornecedor);
    public abstract ArrayList<Fornecedor> consultarFornecedores();
    public String getMensagem();
}
