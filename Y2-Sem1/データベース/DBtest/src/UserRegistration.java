//JCDB API���C���|�[�g����
import java.sql.*;
import java.util.Scanner;
public class UserRegistration{
	public static void main(String[] args) throws Exception{
		System.out.println("�`�`�`���[�U�o�^�����`�`�`\n");

		//�f�[�^�x�[�X�ڑ��ɕK�v�ȕϐ���錾
		Connection conn = null;
		Statement st = null;
		ResultSet rs = null;

		try{
			//�X�L���i�[�C���X�^���X��
			Scanner sc = new Scanner(System.in);
			//�e���ڂ̓��͂��s��
			System.out.print("���O����͂��Ă��������F");
			String uname = sc.nextLine();
			System.out.print("�ӂ肪�Ȃ���͂��Ă��������F");
			String ufname = sc.nextLine();
			System.out.print("���[���A�h���X����͂��Ă��������F");
			String email = sc.nextLine();
			System.out.print("�p�X���[�h����͂��Ă��������F");
			String password = sc.nextLine();
			System.out.print("�d�b�ԍ�����͂��Ă��������F");
			String tel = sc.nextLine();

			//�J�[�h�ԍ��͔C�ӂȂ̂ŁA����ɂ�菈���𕪊�
			System.out.print("�J�[�h�ԍ���o�^���܂����H y�u�͂��v�A����ȊO�u�������v�F");
			String cardans = sc.nextLine();
			String cardnum = "NULL";
			if (cardans.equals("y")) {
				System.out.print("�J�[�h�ԍ�����͂��Ă��������F");
				cardnum = sc.nextLine();
			}

			//���͂���͕����Ή�����̂Ŕz��ŊǗ�
			String[] address = new String[9];
			String[] postnum = new String[9];
			int i = 0;
			System.out.print("�X�֔ԍ�����͂��Ă��������F");
			postnum[i] = sc.nextLine();
			System.out.print("���͂���Z������͂��Ă��������F");
			address[i] = sc.nextLine();

			// �ʂ̂��͂��悪����ԁA�������[�v
			while (true) {
				System.out.print("�ʂ̂��͂����o�^���܂����H y�u�͂��v�A����ȊO�u�������v�F");
				String addans = sc.nextLine();
				if (addans.equals("y")) {
					i++;
					System.out.print("�X�֔ԍ�����͂��Ă��������F");
					postnum[i] = sc.nextLine();
					System.out.print("���͂���Z������͂��Ă��������F");
					address[i] = sc.nextLine();
				}else{
					break;
				}
			}
			System.out.println("�`�`�`�f�[�^�x�[�X�ɓo�^���`�`�`\n");
			
			//�h���C�o��ǂݍ���(���ϐ���CLASSPAHT�̐ݒ肪�K�v)
			Class.forName("com.mysql.cj.jdbc.Driver");
			
			//�f�[�^�x�[�X���
			String dbname = "studbY2";   //�ڑ��f�[�^�x�[�X
			String dbuser = "dbuser";  //�f�[�^�x�[�X���[�U
			String dbpass = "ecc";     //���O�C���p�X���[�h

			//JDBC�h���C�o���ݒ�
			String dbinfo = "jdbc:mysql://localhost:3306/"+dbname+"?characterEncoding=UTF-8&serverTimezone=Asia/Tokyo";

			//�f�[�^�x�[�X�ɐڑ�����
			conn = DriverManager.getConnection(dbinfo, dbuser, dbpass);
			conn.setAutoCommit(false); //�I�[�g�R�~�b�g�𖳌�
			st = conn.createStatement();

			//Insert�������s����(User�\)
			String usersql  = "INSERT INTO USER (UNAME, RUBY, EMAIL, PASSWORD, TEL, CARD_NO) ";
			 	   usersql += "VALUES ('" + uname +"', '" + ufname + "', '" + email + "', '" + password +"','" + tel + "','" + cardnum + "' )";
			System.out.println(usersql);
			st.executeUpdate(usersql);

			//Insert�������s����(Deliaddress�\)
			String usersearch = "SELECT USER_NO FROM USER WHERE UNAME LIKE '%" + uname + "%'";
			rs = st.executeQuery(usersearch);

			String userno = null;
			while( rs.next() ){
				userno   = rs.getString("USER_NO");
				System.out.println(userno);
			}

			for (int j = 0; j <= i; j++) {
				String addresssql = "INSERT INTO Deliaddress (USER_NO, DELI_NO, POST_NO, ADDRESS) ";
				addresssql += "VALUES ('" + userno + "', '" + (j + 1) + "', '" + postnum[j] + "', '" + address[j] + "' )";
				System.out.println(addresssql);
				st.executeUpdate(addresssql);
			}

			//����I���Ȃ�R�~�b�g
			conn.commit();
			System.out.println("�R�~�b�g���܂���");
			System.out.println("�`�`�`�o�^�������������܂����`�`�`\n");

		}catch(Exception e){
			//�G���[�̏ꍇ�́A���[���o�b�N���s���B
			if(conn != null){
				System.out.println("�`�`�`�o�^�������ُ�I�����܂����`�`�`\n");
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
