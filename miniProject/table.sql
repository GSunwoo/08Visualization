create table g_deliv(
	idx number primary key,
	sigun varchar2(20) not  null,
	str varchar2(100) not  null,
	addr varchar2(200) not  null,
	latitude number(20,10) not  null,
	longitude number(20,10) not  null
);

create sequence g_deliv_seq
    increment by 1 /*증가치 : 1 */
    start with 1   /*초기값(시작값) : 1 */
    minvalue 1     /*최소값 : 1 */
    nomaxvalue     /*최대값 : x */
    nocycle        /*사이클 사용 x*/
    nocache;       /*캐시메모리 사용 x*/