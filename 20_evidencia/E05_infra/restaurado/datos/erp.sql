--
-- PostgreSQL database dump
--

\restrict cO4jkQhFq2uPPodkIMMP3rYrhcOVLGNAVPkhgXRLU6pcFLw4yefN2zwQ3xXQ9JR

-- Dumped from database version 16.15 (Debian 16.15-1.pgdg13+2)
-- Dumped by pg_dump version 16.15 (Debian 16.15-1.pgdg13+2)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: audit_lab; Type: TABLE; Schema: public; Owner: erp_app
--

CREATE TABLE public.audit_lab (
    id integer NOT NULL,
    nota text
);


ALTER TABLE public.audit_lab OWNER TO erp_app;

--
-- Data for Name: audit_lab; Type: TABLE DATA; Schema: public; Owner: erp_app
--

COPY public.audit_lab (id, nota) FROM stdin;
1	registro de prueba
\.


--
-- Name: audit_lab audit_lab_pkey; Type: CONSTRAINT; Schema: public; Owner: erp_app
--

ALTER TABLE ONLY public.audit_lab
    ADD CONSTRAINT audit_lab_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict cO4jkQhFq2uPPodkIMMP3rYrhcOVLGNAVPkhgXRLU6pcFLw4yefN2zwQ3xXQ9JR

