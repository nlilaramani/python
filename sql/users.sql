-- Table: ecommerce.user

-- DROP TABLE ecommerce."user";

CREATE TABLE ecommerce."user"
(
    id smallint NOT NULL DEFAULT nextval('ecommerce.user_id_seq'::regclass),
    username character varying(20) COLLATE pg_catalog."default",
    password character varying(20) COLLATE pg_catalog."default",
    fname character varying(50) COLLATE pg_catalog."default",
    lname character varying COLLATE pg_catalog."default",
    email character varying COLLATE pg_catalog."default",
    CONSTRAINT user_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE ecommerce."user"
    OWNER to postgres;
