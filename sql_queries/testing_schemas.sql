insert into investment_objective values('1','io1',0)
truncate investment_objective
insert into investor 
	values('n1','e1',100,70,'1234567890','add1','pass1',30,'1')
truncate investor
select investor_password from investor where investor_email = 'e1'

select * from investor

insert into investor values('n1','e1@gmail.com','pass1','100','1234567890

INSERT INTO company VALUES
	('00',29,'SBI','3','ABC',100.000,2000.000,30.000,'https://en.wikipedia.org/wiki/SBI_Mutual_Fund'),
	('11',13,'ICICI','4','DEF',30.000,1000.000,50.000,'https://en.wikipedia.org/wiki/ICICI_Prudential_Mutual_Fund'),
	('22',23,'Reliance','5','GHI',10.000,100.000,20.000,'https://en.wikipedia.org/wiki/Reliance_Industries'),
	('33',7,'Adani','1','JKL',70.000,190.000,40.000,''),
	('44',45,'Tata','4','MNO',120.000,500.000,100.000,'');

							
INSERT INTO 
    investment_objective (objective_id, objective_name, no_of_investors_invested)
VALUES
    ('1','Capital preservation','32'),
	('2','Income generation','46'),
	('3','Capital growth','67'),
	('4','Speculation','33'),
	('5','Socially responsible investing','27');
		
truncate investment_option
insert into investment_option values
							('1','Stocks','Ownership shares in a company that entitle the holder to a portion of the companys profits.'),
 							('2','Bonds','Fixed-income securities that represent a loan made by an investor to a borrower, typically a government or corporation.'),
 							('3','Mutual funds','Pooled investment vehicles that invest in a diversified portfolio of stocks, bonds, or other securities'),
 							('4','Exchange-traded funds','Similar to mutual funds, but traded on stock exchanges like individual stocks.'), 							
							('5','Real estate','Investing in physical property such as rental properties, commercial properties, or raw land.'),
 							('6','Commodities','Investing in physical goods such as gold, silver, oil, or agricultural products.'),
 							('7','Cryptocurrencies','Digital currencies that use cryptography to secure transactions and control the creation of new units.'),
 							('8','Custom Options','Contracts that give the buyer the right, but not the obligation, to buy or sell an underlying asset at a predetermined price'),
 							('9','Futures',' Contracts to buy or sell an underlying asset at a predetermined price and date in the future.'),
 							('10','Certificates of deposit',' Time deposits offered by banks and credit unions that pay a fixed interest rate over a set period of time.');
							
							
							
							
	