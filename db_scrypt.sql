-- public."Roles" definition

-- Drop table

-- DROP TABLE "Roles";

CREATE TABLE "Roles" (
	id int4 NOT NULL DEFAULT nextval('roles_id_seq'::regclass),
	"name" varchar(20) NULL,
	description varchar(255) NULL,
	CONSTRAINT roles_pkey PRIMARY KEY (id)
);


-- public."Users" definition

-- Drop table

-- DROP TABLE "Users";

CREATE TABLE "Users" (
	id uuid NOT NULL DEFAULT gen_random_uuid(),
	"name" varchar(200) NOT NULL,
	lastname varchar(200) NOT NULL,
	secondlastname varchar(200) NULL,
	email varchar(200) NOT NULL,
	"password" varchar(400) NOT NULL,
	image varchar NOT NULL,
	active bool NULL DEFAULT true,
	CONSTRAINT users_email_key UNIQUE (email),
	CONSTRAINT users_pkey PRIMARY KEY (id)
);


-- public."UserRoles" definition

-- Drop table

-- DROP TABLE "UserRoles";

CREATE TABLE "UserRoles" (
	id uuid NOT NULL DEFAULT gen_random_uuid(),
	userid uuid NULL,
	roleid int4 NULL,
	CONSTRAINT usersroles_pkey PRIMARY KEY (id),
	CONSTRAINT usersroles_roleid_fkey FOREIGN KEY (roleid) REFERENCES "Roles"(id),
	CONSTRAINT usersroles_userid_fkey FOREIGN KEY (userid) REFERENCES "Users"(id)
);

