insert into investment_objective values('id1','io1',0)

insert into investor 
	values('n1','e1',100,70,'1234567890','add1','pass1',30,'id1')

select investor_password from investor where investor_email = 'e1'


investor_name varchar(200),
	investor_email varchar(200),
	investor_budget numeric,
	investor_total_investment_amount numeric,
	investor_mobile_no char(10),
	investor_address varchar(200),
	investor_password varchar(200),
	investor_age int,
	fk_investment_objective_id varchar(200),


