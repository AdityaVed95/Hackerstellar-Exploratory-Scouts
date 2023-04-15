insert into investment_objective values('1','io1',0)
truncate investment_objective
insert into investor 
	values('n1','e1',100,70,'1234567890','add1','pass1',30,'1')
truncate investor
select investor_password from investor where investor_email = 'e1'

select * from investor

insert into investor values('n1','e1@gmail.com','pass1','100','1234567890

INSERT INTO company VALUES
	('00',29,'SBI Mutual Fund','3','ABC',100.000,2000.000,30.000,'https://en.wikipedia.org/wiki/SBI_Mutual_Fund'),
	('11',13,'ICICI Prudential Mutual Fund','4','DEF',30.000,1000.000,50.000,'https://en.wikipedia.org/wiki/ICICI_Prudential_Mutual_Fund'),
	('22',23,'c3','5','GHI',10.000,100.000,20.000,''),
	('33',7,'c4','1','JKL',70.000,190.000,40.000,''),
	('44',45,'c5','4','MNO',120.000,500.000,100.000,'');

							
INSERT INTO 
    investment_objective (objective_id, objective_name, no_of_investors_invested)
VALUES
    ('1','Capital preservation','32'),
	('2','Income generation','46'),
	('3','Capital growth','67'),
	('4','Speculation','33'),
	('5','Socially responsible investing','27');
							
insert into investment_option values
							('1','Stocks'),
							('2','Bonds'),
							('3','Mutual funds'),
							('4','Exchange-traded funds'),
							('5','Real estate'),
							('6','Commodities'),
							('7','Cryptocurrencies'),
							('8','CustomOptions'),
							('9','Futures'),
							('10','Certificates_of_deposit');
							
							
							
							
	