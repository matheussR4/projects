/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package bancodedados;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 *
 * @author Petheus Rodrigues
 */
public class ConexaoBanco {
    private Connection conexao;
    private String driver;
    private String url, usuario, senha;
    private String mensagem;
    private static boolean conectado = false;
    private static ConexaoBanco conexaoBanco = null;
    
    private ConexaoBanco(){
        driver = "com.mysql.jdbc.Driver";
        url = "jdbc:mysql://localhost/farmaciajsml";
    }

    public Connection getConexao() {
        return conexao;
    }

    public String getMensagem() {
        return mensagem;
    }

    public static boolean isConectado() {
        return conectado;
    }
    
    public static ConexaoBanco getInstanceConexaoBanco(){
        if (conexaoBanco == null){
            conexaoBanco = new ConexaoBanco();
        }
        return conexaoBanco;
    }
    
    public boolean abrirConexao(String url, String usuario,
                                String senha){
        //this.url += url;
        this.senha = "mysql-mr4";
        this.usuario = "root";
        
        try {
            Class.forName(driver);
            conexao = DriverManager.getConnection(this.url, this.usuario, this.senha);
            mensagem = "Conexão realizada com sucesso.";
            conectado = true;
            return true;
        } catch (ClassNotFoundException | SQLException ex) {
            mensagem = ex.getMessage();
            return false;
        }
    }
    
    public boolean fecharConexao(){
        if (conectado){
            try {
                conexao.close();
                mensagem = "Conexão fechada com sucesso.";
                return true;
            } catch (SQLException ex) {
                mensagem = ex.getMessage();
                return false;
            } catch (Exception ex){
                mensagem = ex.getMessage();
                return false;
            }
        }
        mensagem = "A conexão já estava fechada";
        return false;
    }
}
