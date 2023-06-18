//JCDB API���C���|�[�g����
import java.sql.*;

public class MySQLConnect{

    public static void main(String[] args) throws Exception{

        System.out.println("MySQL�ڑ��v���O�����J�n\n");
		
		//�f�[�^�x�[�X�ڑ��ɕK�v�ȕϐ���錾
        Connection conn = null;
        Statement st = null;
        ResultSet rs = null;

        try{
            //�h���C�o��ǂݍ���(���ϐ���CLASSPAHT�̐ݒ肪�K�v)
            Class.forName("com.mysql.cj.jdbc.Driver");

            //�f�[�^�x�[�X���
            String dbname = "studb";   //�ڑ��f�[�^�x�[�X
            String dbuser = "dbuser";  //�f�[�^�x�[�X���[�U
            String dbpass = "ecc";     //���O�C���p�X���[�h

            //JDBC�h���C�o���ݒ�
            String dbinfo = 
                "jdbc:mysql://localhost/"+dbname+"?characterEncoding=UTF-8&serverTimezone=JST";

            //�f�[�^�x�[�X�ɐڑ�����
            conn = DriverManager.getConnection(dbinfo, dbuser, dbpass);
			conn.setAutoCommit(false); //�I�[�g�R�~�b�g�𖳌�
			
            st = conn.createStatement();
			
			//INSERT�����쐬����
			String isql  = "INSERT INTO product (product_no, pname, category, price ) ";
			       isql += "VALUES ('1015', '�o�i�i�A�C�X', '�T�C�h', 370 )";
			
			//SQL�����o�͂��Ă���
		    System.out.println(isql); 
			
			//executeUpdate�֐���UPDATE�AINSERT�܂��́ACREATE�Ȃǂ�DDL�������s�ł���B
			//�߂�l�́A�f�[�^��������
			int cnt = st.executeUpdate(isql);
            System.out.println(cnt +"���̃f�[�^��o�^���܂���\n");
			
			
            //SELECT���𑗐M����
            String ssql = "SELECT * FROM product WHERE pname LIKE '%�A�C�X%'";
			//SQL�����o�͂��Ă���
		    System.out.println(ssql); 

            //SELECT���̏ꍇ�́AexecuteQuery�֐����g�p����B
			//������͎��s���ʂ��߂�l�ɂȂ�̂Ō��ʂ��f�[�^�Z�b�g�Ɋi�[����
            rs = st.executeQuery(ssql);

            //�f�[�^�x�[�X�̒l���󂯎��ϐ��錾
            String productNo;
            String productName;
            String category;
            int price;
			
            //�f�[�^�Z�b�g�Ƀf�[�^�����݂���ԌJ��Ԃ�
            while(rs.next()){

                productNo   = rs.getString("PRODUCT_NO");
                productName = rs.getString("PNAME");
                category    = rs.getString("CATEGORY");
                price       = rs.getInt("PRICE");

                // �P�s���Ƃɏ��i������ʂɏo�͂���
                String wkSt = "���i�ԍ��F"+ productNo +
                              " ���i���F"+ productName +
                              " �J�e�S���F"+ category +
                              " ���i�F" + price ;
                System.out.println(wkSt);
            }
			
			//�n���Y�I���ׁ̈A���[���o�b�N���s���B
			conn.rollback();
		    System.out.println("\n���[���o�b�N���܂���"); 


        }catch(Exception e){
			
			//�G���[�̏ꍇ�́A���[���o�b�N���s���B
			if(conn != null){
				conn.rollback();
			}

            e.printStackTrace();

        }finally{

            //MySQL�Ƃ̐ڑ���ؒf����
			if(rs != null){ rs.close(); }
            if(st != null){ st.close(); }
            if(conn != null){ conn.close(); }

        }
    }
}

