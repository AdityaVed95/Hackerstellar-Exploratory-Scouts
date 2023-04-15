CREATE TABLE investment_objective(

	objective_id varchar(200),
	objective_name varchar(200),
	no_of_investors_invested int,
	PRIMARY KEY (objective_id)

)


CREATE TABLE investor(

	investor_name varchar(200),
	investor_email varchar(200),
	invest_fifty_plus int,
	investor_mobile_no char(10),
	investor_address varchar(200),
	investor_password varchar(200),
	investor_age int,
	fk_investment_objective_id varchar(200),
	PRIMARY KEY(investor_email),
	FOREIGN KEY(fk_investment_objective_id) references investment_objective(objective_id)
	
)

CREATE TABLE companies(

	company_id varchar(200),
	no_of_customers_investing int,
	company_name varchar(200),
	PRIMARY KEY(company_id)
	fk_company_primary_investment_objective_id 
	 
)

