//JCDB API���C���|�[�g����
import java.sql.*;
import java.util.ArrayList;
import java.util.Scanner;

public class UserRegistration{
	
	public static void main(String[] args) throws Exception{
		System.out.println("�`�`�`���[�U�o�^�����`�`�`\n");
		//�f�[�^�x�[�X�ڑ��ɕK�v�ȕϐ���錾
		Connection conn = null;
		Statement st = null;
		try{
			//�X�L���i�[�C���X�^���X��
			Scanner sc = new Scanner(System.in);
			
			//�e���ڂ̓��͂��s��
			System.out.print("���O����͂��Ă��������F");
			String uname = sc.nextLine();
			
			
			//�J�[�h�ԍ��͔C�ӂȂ̂ŁA����ɂ�菈���𕪊�
			
			
			//���͂���͕����Ή�����̂Ŕz��ŊǗ�
			
			
			
			// �ʂ̂��͂��悪����ԁA�������[�v
			
			
			
			System.out.println("�`�`�`�f�[�^�x�[�X�ɓo�^���`�`�`\n");
			
			//�h���C�o��ǂݍ���(���ϐ���CLASSPAHT�̐ݒ肪�K�v)
			Class.forName("com.mysql.cj.jdbc.Driver");
			
			//�f�[�^�x�[�X���
			
			
			
			//JDBC�h���C�o���ݒ�
			
			
			
			//�f�[�^�x�[�X�ɐڑ�����
			
			
			
			//Insert�������s����(User�\)
			
			
			
			//Insert�������s����(Deliaddress�\)
			
			
			
			//����I���Ȃ�R�~�b�g
			
			
			
			System.out.println("�`�`�`�o�^�������������܂����`�`�`\n");
		}catch(Exception e){
			//�G���[�̏ꍇ�́A���[���o�b�N���s���B
			if(conn != null){
				System.out.println("�`�`�`�o�^�������ُ�I�����܂����`�`�`\n");
			}
			e.printStackTrace();
		}finally{
			//MySQL�Ƃ̐ڑ���ؒf����
			if(st != null){ st.close(); }
			if(conn != null){ conn.close(); }
			
		}
	}
}
