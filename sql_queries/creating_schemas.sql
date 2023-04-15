CREATE TABLE investment_objective(

	objective_id varchar(200),
	objective_name varchar(200),
	no_of_investors_invested int,
	PRIMARY KEY (objective_id)

)


CREATE TABLE investor(

	investor_name varchar(200),
	investor_email varchar(200),
	investor_budget numeric,
	investor_total_investment_amount numeric,
	investor_mobile_no char(10),
	investor_address varchar(200),
	investor_password varchar(200),
	investor_age int,
	fk_investment_objective_id varchar(200),
	PRIMARY KEY(investor_email),
	FOREIGN KEY(fk_investment_objective_id) references investment_objective(objective_id)
	
)

CREATE TABLE company(

	company_id varchar(200),
	no_of_customers_investing int,
	company_name varchar(200),
	fk_company_primary_investment_objective_id varchar(200),
	company_industry varchar(200),
	company_stock_price numeric,
	company_revenue numeric,
	company_profit numeric,
	PRIMARY KEY(company_id),
	FOREIGN KEY(fk_company_primary_investment_objective_id) references investment_objective(objective_id)

	 
)

CREATE TABLE investor_company(

	fk_investor_email varchar(200),
	fk_company_id varchar(200),
	PRIMARY KEY(fk_investor_email,fk_company_id),
	FOREIGN KEY(fk_investor_email) references investor(investor_email),
	FOREIGN KEY(fk_company_id) references company(company_id)
)

-- create table tempo(

-- 	sal	numeric
-- )

-- insert into tempo values(10.4342)
-- select * from tempo

