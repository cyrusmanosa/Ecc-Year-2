/*
�f�[�^�x�[�X���KII 3�T��
�N���X�FSK2A03
����ҁF���Ər
�쐬���F2023/04/28
*/

/*
����́A�ڑ����̐ݒ�ƃ��[�U�̌������Ǘ����邱�ƂŃZ�L�����e�B�̌���ɂ��Ċw�K�����܂����B
�ۑ�ł́Adbuser�̃Z�L�����e�B���グ��Ƌ��ɁA�O������ڑ��ł��郆�[�U�̃Z�L�����e�B��
�l�����č쐬���Ă����܂��B
*/

--��P�Fdbuser��localhost����̂�MySQL�ɐڑ��ł���悤�ɂ��Ă��������B

RENAME USER dbuser TO dbuser@localhost;
SELECT USER,HOST FROM MYSQL.USER WHERE USER='dbuser';

--��Q�F�ǂ̐ڑ�������A�N�Z�X�ł���dbshow���[�U���쐬���Ă��������B

CREATE USER dbshow
IDENTIFIED WITH MYSQL_NATIVE_PASSWORD BY 'ecc';
SELECT USER,HOST FROM MYSQL.USER WHERE USER='dbshow';

--��R�Fdbshow�͊O������A�N�Z�X�ł��邽�߁A�f�[�^�̌����̂݋����܂��B
--      studb�f�[�^�x�[�X�ɑ΂���SELECT������t�^���Ă��������B

GRANT USAGE ON *.* TO dbshow;
GRANT SELECT ON studbY2.* TO dbshow;
SHOW GRANTS FOR dbshow;

--��S�Fdbshow���[�U�Ń��O�C�����āA���i���ɃT���_���܂܂�Ă��鏤�i��
--      �\�����Ă��������B

SELECT * FROM PRODUCT WHERE PNAME LIKE '%�T���_';

--��T�Fdbshow���[�U�ŃV�[�U�[�T���_�̏��i���i��500�ɍX�V�������Ă��������B

UPDATE product SET PRICE = '500' WHERE PNAME = �e�V�[�U�[�T���_�f;
SELECT * FROM product WHERE pname = �e�V�[�U�[�T���_�f;

--��U�Fdbtest���[�U�ɏ��i�\�̌����A�}���A�X�V�A�폜������t�^���Ă��������B

GRANT SELECT,INSERT,UPDATE,DELETE ON studbY2.product TO dbtest@localhost;
SHOW GRANTS FOR dbtest@localhost;

--��V�Fdbtest���[�U�ŃV�[�U�[�T���_�̏��i���i��500�ɍX�V���Ă��������B
--      �f�[�^�m�F��A�g�����U�N�V�������������Ă��������B

UPDATE PRODUCT SET PRICE = 500 WHERE PNAME = '�V�[�U�[�T���_';
SELECT * FROM product WHERE PNAME LIKE '%�T���_';

Rollback;


/*
�n���Y�I����Root���[�U�̃p�X���[�h��ύX���܂����B
Root�p�X���[�h�̃��Z�b�g���@�Ō��̃p�X���[�h�ɕύX���܂��B
*/


--��W�F�ݒ�t�@�C����ҏW���āA�F�؂̖����������Ă��������B
--      �ύX�����I�v�V�������񓚂��Ă��������B
/*
�ݒ�I�v�V�����F MAC�ł�����B�B�B�B�B�B
*/


--��X�Froot���[�U�̃p�X���[�h��root�ɕύX���Ă��������B

alter user 'root'@'localhost' identified by 'root';
set password for root@localhost = 'root';



--��P�O�F�ݒ�t�@�C����ҏW���āA�F�؂̗L���������Ă��������B
--        �ύX�����I�v�V�������񓚂��Ă��������B
/*
�ݒ�I�v�V�����FMAC�ł�����B�B�B�B�B�B
*/


