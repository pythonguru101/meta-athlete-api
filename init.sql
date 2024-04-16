--
-- PostgreSQL database dump
--

-- Dumped from database version 14.6
-- Dumped by pg_dump version 15.1

-- Started on 2023-04-05 13:34:22 CST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: linroot
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO linroot;

--
-- TOC entry 842 (class 1247 OID 16448)
-- Name: cardtype; Type: TYPE; Schema: public; Owner: linpostgres
--

CREATE TYPE public.cardtype AS ENUM (
    'GOLD',
    'PLATINUM',
    'DIAMOND'
);


ALTER TYPE public.cardtype OWNER TO linpostgres;

--
-- TOC entry 839 (class 1247 OID 16436)
-- Name: schoolgrade; Type: TYPE; Schema: public; Owner: linpostgres
--

CREATE TYPE public.schoolgrade AS ENUM (
    'ELEMENTARY_SCHOOL',
    'MIDDLE_SCHOOL',
    'JUNIOR_HIGH_SCHOOL',
    'SENIOR_HIGH_SCHOOL',
    'PREPARATORY_SCHOOL'
);


ALTER TYPE public.schoolgrade OWNER TO linpostgres;

--
-- TOC entry 836 (class 1247 OID 16406)
-- Name: sporttype; Type: TYPE; Schema: public; Owner: linpostgres
--

CREATE TYPE public.sporttype AS ENUM (
    'BASEBALL',
    'BASKETBALL',
    'CHEERLEADING',
    'CROSS_COUNTRY',
    'FIELD_HOCKEY',
    'FOOTBALL',
    'GYMNASTICS',
    'ICE_HOCKEY',
    'SOCCER',
    'SOFTBALL',
    'SWIMMING',
    'TENNIS',
    'VOLLEYBALL',
    'WRESTLING'
);


ALTER TYPE public.sporttype OWNER TO linpostgres;

--
-- TOC entry 833 (class 1247 OID 16395)
-- Name: usertype; Type: TYPE; Schema: public; Owner: linpostgres
--

CREATE TYPE public.usertype AS ENUM (
    'ATHLETE',
    'COACH',
    'REFEREE',
    'FAN',
    'CAPTAIN'
);


ALTER TYPE public.usertype OWNER TO linpostgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 16576)
-- Name: avail_tier_cards; Type: TABLE; Schema: public; Owner: linpostgres
--

CREATE TABLE public.avail_tier_cards (
    p_id integer NOT NULL,
    card_number integer NOT NULL,
    tier character varying NOT NULL,
    id_nft integer NOT NULL
);


ALTER TABLE public.avail_tier_cards OWNER TO linpostgres;

--
-- TOC entry 219 (class 1259 OID 16575)
-- Name: athletes_cards_p_id_seq; Type: SEQUENCE; Schema: public; Owner: linpostgres
--

CREATE SEQUENCE public.athletes_cards_p_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.athletes_cards_p_id_seq OWNER TO linpostgres;

--
-- TOC entry 4122 (class 0 OID 0)
-- Dependencies: 219
-- Name: athletes_cards_p_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: linpostgres
--

ALTER SEQUENCE public.athletes_cards_p_id_seq OWNED BY public.avail_tier_cards.p_id;


--
-- TOC entry 214 (class 1259 OID 16529)
-- Name: files; Type: TABLE; Schema: public; Owner: linpostgres
--

CREATE TABLE public.files (
    p_id integer NOT NULL,
    file_url character varying NOT NULL
);


ALTER TABLE public.files OWNER TO linpostgres;

--
-- TOC entry 213 (class 1259 OID 16528)
-- Name: files_p_id_seq; Type: SEQUENCE; Schema: public; Owner: linpostgres
--

CREATE SEQUENCE public.files_p_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.files_p_id_seq OWNER TO linpostgres;

--
-- TOC entry 4123 (class 0 OID 0)
-- Dependencies: 213
-- Name: files_p_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: linpostgres
--

ALTER SEQUENCE public.files_p_id_seq OWNED BY public.files.p_id;


--
-- TOC entry 210 (class 1259 OID 16456)
-- Name: health_services; Type: TABLE; Schema: public; Owner: linpostgres
--

CREATE TABLE public.health_services (
    p_id integer NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(120) NOT NULL
);


ALTER TABLE public.health_services OWNER TO linpostgres;

--
-- TOC entry 209 (class 1259 OID 16455)
-- Name: health_services_p_id_seq; Type: SEQUENCE; Schema: public; Owner: linpostgres
--

CREATE SEQUENCE public.health_services_p_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.health_services_p_id_seq OWNER TO linpostgres;

--
-- TOC entry 4124 (class 0 OID 0)
-- Dependencies: 209
-- Name: health_services_p_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: linpostgres
--

ALTER SEQUENCE public.health_services_p_id_seq OWNED BY public.health_services.p_id;


--
-- TOC entry 216 (class 1259 OID 16538)
-- Name: nft_athlete_card; Type: TABLE; Schema: public; Owner: linpostgres
--

CREATE TABLE public.nft_athlete_card (
    p_id integer NOT NULL,
    name character varying NOT NULL,
    nft_uuid character varying,
    kind character varying NOT NULL,
    sport character varying NOT NULL,
    birthdate timestamp without time zone NOT NULL,
    weight numeric NOT NULL,
    height numeric NOT NULL,
    schoolgrade character varying NOT NULL,
    photo integer,
    "cardMinted" boolean DEFAULT false,
    quantity_gold integer DEFAULT 0,
    quantity_platinum integer DEFAULT 0,
    quantity_diamond integer DEFAULT 0
);


ALTER TABLE public.nft_athlete_card OWNER TO linpostgres;

--
-- TOC entry 218 (class 1259 OID 16556)
-- Name: nft_athlete_card_marketplace; Type: TABLE; Schema: public; Owner: linpostgres
--

CREATE TABLE public.nft_athlete_card_marketplace (
    p_id integer NOT NULL,
    wallet_id character varying,
    tier character varying NOT NULL,
    price integer NOT NULL,
    athlete_card_id integer
);


ALTER TABLE public.nft_athlete_card_marketplace OWNER TO linpostgres;

--
-- TOC entry 217 (class 1259 OID 16555)
-- Name: nft_athlete_card_marketplace_p_id_seq; Type: SEQUENCE; Schema: public; Owner: linpostgres
--

CREATE SEQUENCE public.nft_athlete_card_marketplace_p_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.nft_athlete_card_marketplace_p_id_seq OWNER TO linpostgres;

--
-- TOC entry 4125 (class 0 OID 0)
-- Dependencies: 217
-- Name: nft_athlete_card_marketplace_p_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: linpostgres
--

ALTER SEQUENCE public.nft_athlete_card_marketplace_p_id_seq OWNED BY public.nft_athlete_card_marketplace.p_id;


--
-- TOC entry 215 (class 1259 OID 16537)
-- Name: nft_athlete_card_p_id_seq; Type: SEQUENCE; Schema: public; Owner: linpostgres
--

CREATE SEQUENCE public.nft_athlete_card_p_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.nft_athlete_card_p_id_seq OWNER TO linpostgres;

--
-- TOC entry 4126 (class 0 OID 0)
-- Dependencies: 215
-- Name: nft_athlete_card_p_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: linpostgres
--

ALTER SEQUENCE public.nft_athlete_card_p_id_seq OWNED BY public.nft_athlete_card.p_id;


--
-- TOC entry 212 (class 1259 OID 16518)
-- Name: user; Type: TABLE; Schema: public; Owner: linpostgres
--

CREATE TABLE public."user" (
    p_id integer NOT NULL,
    username character varying NOT NULL,
    password character varying NOT NULL,
    wallet_id character varying NOT NULL,
    did character varying,
    vc character varying
);


ALTER TABLE public."user" OWNER TO linpostgres;

--
-- TOC entry 211 (class 1259 OID 16517)
-- Name: user_p_id_seq; Type: SEQUENCE; Schema: public; Owner: linpostgres
--

CREATE SEQUENCE public.user_p_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_p_id_seq OWNER TO linpostgres;

--
-- TOC entry 4127 (class 0 OID 0)
-- Dependencies: 211
-- Name: user_p_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: linpostgres
--

ALTER SEQUENCE public.user_p_id_seq OWNED BY public."user".p_id;


--
-- TOC entry 3942 (class 2604 OID 16579)
-- Name: avail_tier_cards p_id; Type: DEFAULT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.avail_tier_cards ALTER COLUMN p_id SET DEFAULT nextval('public.athletes_cards_p_id_seq'::regclass);


--
-- TOC entry 3935 (class 2604 OID 16532)
-- Name: files p_id; Type: DEFAULT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.files ALTER COLUMN p_id SET DEFAULT nextval('public.files_p_id_seq'::regclass);


--
-- TOC entry 3933 (class 2604 OID 16459)
-- Name: health_services p_id; Type: DEFAULT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.health_services ALTER COLUMN p_id SET DEFAULT nextval('public.health_services_p_id_seq'::regclass);


--
-- TOC entry 3936 (class 2604 OID 16541)
-- Name: nft_athlete_card p_id; Type: DEFAULT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.nft_athlete_card ALTER COLUMN p_id SET DEFAULT nextval('public.nft_athlete_card_p_id_seq'::regclass);


--
-- TOC entry 3941 (class 2604 OID 16559)
-- Name: nft_athlete_card_marketplace p_id; Type: DEFAULT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.nft_athlete_card_marketplace ALTER COLUMN p_id SET DEFAULT nextval('public.nft_athlete_card_marketplace_p_id_seq'::regclass);


--
-- TOC entry 3934 (class 2604 OID 16521)
-- Name: user p_id; Type: DEFAULT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN p_id SET DEFAULT nextval('public.user_p_id_seq'::regclass);


--
-- TOC entry 4115 (class 0 OID 16576)
-- Dependencies: 220
-- Data for Name: avail_tier_cards; Type: TABLE DATA; Schema: public; Owner: linpostgres
--

COPY public.avail_tier_cards (p_id, card_number, tier, id_nft) FROM stdin;
1	1	GOLD	1
2	2	GOLD	1
\.


--
-- TOC entry 4109 (class 0 OID 16529)
-- Dependencies: 214
-- Data for Name: files; Type: TABLE DATA; Schema: public; Owner: linpostgres
--

COPY public.files (p_id, file_url) FROM stdin;
1	https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Donald_Trump_official_portrait.jpg/220px-Donald_Trump_official_portrait.jpg
\.


--
-- TOC entry 4105 (class 0 OID 16456)
-- Dependencies: 210
-- Data for Name: health_services; Type: TABLE DATA; Schema: public; Owner: linpostgres
--

COPY public.health_services (p_id, name, code) FROM stdin;
\.


--
-- TOC entry 4111 (class 0 OID 16538)
-- Dependencies: 216
-- Data for Name: nft_athlete_card; Type: TABLE DATA; Schema: public; Owner: linpostgres
--

COPY public.nft_athlete_card (p_id, name, nft_uuid, kind, sport, birthdate, weight, height, schoolgrade, photo, "cardMinted", quantity_gold, quantity_platinum, quantity_diamond) FROM stdin;
1	The Special	\N	Fan	NBL	2023-04-05 18:29:52.082918	75	15	B	1	f	1	0	0
\.


--
-- TOC entry 4113 (class 0 OID 16556)
-- Dependencies: 218
-- Data for Name: nft_athlete_card_marketplace; Type: TABLE DATA; Schema: public; Owner: linpostgres
--

COPY public.nft_athlete_card_marketplace (p_id, wallet_id, tier, price, athlete_card_id) FROM stdin;
\.


--
-- TOC entry 4107 (class 0 OID 16518)
-- Dependencies: 212
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: linpostgres
--

COPY public."user" (p_id, username, password, wallet_id, did, vc) FROM stdin;
\.


--
-- TOC entry 4128 (class 0 OID 0)
-- Dependencies: 219
-- Name: athletes_cards_p_id_seq; Type: SEQUENCE SET; Schema: public; Owner: linpostgres
--

SELECT pg_catalog.setval('public.athletes_cards_p_id_seq', 1, false);


--
-- TOC entry 4129 (class 0 OID 0)
-- Dependencies: 213
-- Name: files_p_id_seq; Type: SEQUENCE SET; Schema: public; Owner: linpostgres
--

SELECT pg_catalog.setval('public.files_p_id_seq', 1, false);


--
-- TOC entry 4130 (class 0 OID 0)
-- Dependencies: 209
-- Name: health_services_p_id_seq; Type: SEQUENCE SET; Schema: public; Owner: linpostgres
--

SELECT pg_catalog.setval('public.health_services_p_id_seq', 1, false);


--
-- TOC entry 4131 (class 0 OID 0)
-- Dependencies: 217
-- Name: nft_athlete_card_marketplace_p_id_seq; Type: SEQUENCE SET; Schema: public; Owner: linpostgres
--

SELECT pg_catalog.setval('public.nft_athlete_card_marketplace_p_id_seq', 1, false);


--
-- TOC entry 4132 (class 0 OID 0)
-- Dependencies: 215
-- Name: nft_athlete_card_p_id_seq; Type: SEQUENCE SET; Schema: public; Owner: linpostgres
--

SELECT pg_catalog.setval('public.nft_athlete_card_p_id_seq', 1, false);


--
-- TOC entry 4133 (class 0 OID 0)
-- Dependencies: 211
-- Name: user_p_id_seq; Type: SEQUENCE SET; Schema: public; Owner: linpostgres
--

SELECT pg_catalog.setval('public.user_p_id_seq', 1, false);


--
-- TOC entry 3960 (class 2606 OID 16583)
-- Name: avail_tier_cards athletes_cards_pkey; Type: CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.avail_tier_cards
    ADD CONSTRAINT athletes_cards_pkey PRIMARY KEY (p_id);


--
-- TOC entry 3954 (class 2606 OID 16536)
-- Name: files files_pkey; Type: CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.files
    ADD CONSTRAINT files_pkey PRIMARY KEY (p_id);


--
-- TOC entry 3944 (class 2606 OID 16465)
-- Name: health_services health_services_code_key; Type: CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.health_services
    ADD CONSTRAINT health_services_code_key UNIQUE (code);


--
-- TOC entry 3946 (class 2606 OID 16463)
-- Name: health_services health_services_name_key; Type: CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.health_services
    ADD CONSTRAINT health_services_name_key UNIQUE (name);


--
-- TOC entry 3948 (class 2606 OID 16461)
-- Name: health_services health_services_pkey; Type: CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.health_services
    ADD CONSTRAINT health_services_pkey PRIMARY KEY (p_id);


--
-- TOC entry 3958 (class 2606 OID 16563)
-- Name: nft_athlete_card_marketplace nft_athlete_card_marketplace_pkey; Type: CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.nft_athlete_card_marketplace
    ADD CONSTRAINT nft_athlete_card_marketplace_pkey PRIMARY KEY (p_id);


--
-- TOC entry 3956 (class 2606 OID 16549)
-- Name: nft_athlete_card nft_athlete_card_pkey; Type: CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.nft_athlete_card
    ADD CONSTRAINT nft_athlete_card_pkey PRIMARY KEY (p_id);


--
-- TOC entry 3950 (class 2606 OID 16525)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (p_id);


--
-- TOC entry 3952 (class 2606 OID 16527)
-- Name: user user_wallet_id_key; Type: CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_wallet_id_key UNIQUE (wallet_id);


--
-- TOC entry 3964 (class 2606 OID 16584)
-- Name: avail_tier_cards athletes_cards_id_nft_fkey; Type: FK CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.avail_tier_cards
    ADD CONSTRAINT athletes_cards_id_nft_fkey FOREIGN KEY (id_nft) REFERENCES public.nft_athlete_card(p_id);


--
-- TOC entry 3962 (class 2606 OID 16569)
-- Name: nft_athlete_card_marketplace nft_athlete_card_marketplace_athlete_card_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.nft_athlete_card_marketplace
    ADD CONSTRAINT nft_athlete_card_marketplace_athlete_card_id_fkey FOREIGN KEY (athlete_card_id) REFERENCES public.nft_athlete_card(p_id);


--
-- TOC entry 3963 (class 2606 OID 16564)
-- Name: nft_athlete_card_marketplace nft_athlete_card_marketplace_wallet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.nft_athlete_card_marketplace
    ADD CONSTRAINT nft_athlete_card_marketplace_wallet_id_fkey FOREIGN KEY (wallet_id) REFERENCES public."user"(wallet_id);


--
-- TOC entry 3961 (class 2606 OID 16550)
-- Name: nft_athlete_card nft_athlete_card_photo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: linpostgres
--

ALTER TABLE ONLY public.nft_athlete_card
    ADD CONSTRAINT nft_athlete_card_photo_fkey FOREIGN KEY (photo) REFERENCES public.files(p_id);


--
-- TOC entry 4121 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: linroot
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2023-04-05 13:34:31 CST

--
-- PostgreSQL database dump complete
--