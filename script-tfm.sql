USE [master]
GO
/****** Object:  Database [TFM]    Script Date: 15/09/2021 22:23:21 ******/
CREATE DATABASE [TFM]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'TFM', FILENAME = N'D:\Program Files\Microsoft SQL Server\MSSQL15.BI2019\MSSQL\DATA\TFM.mdf' , SIZE = 73728KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'TFM_log', FILENAME = N'D:\Program Files\Microsoft SQL Server\MSSQL15.BI2019\MSSQL\DATA\TFM_log.ldf' , SIZE = 73728KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [TFM] ADD FILEGROUP [Photos] CONTAINS FILESTREAM 
GO
ALTER DATABASE [TFM] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [TFM].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [TFM] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [TFM] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [TFM] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [TFM] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [TFM] SET ARITHABORT OFF 
GO
ALTER DATABASE [TFM] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [TFM] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [TFM] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [TFM] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [TFM] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [TFM] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [TFM] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [TFM] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [TFM] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [TFM] SET  DISABLE_BROKER 
GO
ALTER DATABASE [TFM] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [TFM] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [TFM] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [TFM] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [TFM] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [TFM] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [TFM] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [TFM] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [TFM] SET  MULTI_USER 
GO
ALTER DATABASE [TFM] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [TFM] SET DB_CHAINING OFF 
GO
ALTER DATABASE [TFM] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [TFM] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [TFM] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [TFM] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'TFM', N'ON'
GO
ALTER DATABASE [TFM] SET QUERY_STORE = OFF
GO
USE [TFM]
GO
/****** Object:  Schema [CR]    Script Date: 15/09/2021 22:23:21 ******/
CREATE SCHEMA [CR]
GO
/****** Object:  Table [CR].[T_ATRIBUTOSCLIENTE]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CR].[T_ATRIBUTOSCLIENTE](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[contact] [varchar](50) NULL,
	[month] [varchar](50) NULL,
	[day_of_week] [varchar](50) NULL,
	[duration] [varchar](50) NULL,
	[campaign] [varchar](50) NULL,
	[pdays] [varchar](50) NULL,
	[previous] [varchar](50) NULL,
	[poutcome] [varchar](50) NULL,
	[emp var rate] [varchar](50) NULL,
	[cons price idx] [varchar](50) NULL,
	[cons conf idx] [varchar](50) NULL,
	[euribor3m] [varchar](50) NULL,
	[nr employed] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [CR].[T_CAMPANAS]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CR].[T_CAMPANAS](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[NOMBRE_CAMPAÑA] [varchar](100) NOT NULL,
	[FECHA_INI] [date] NULL,
	[FECHA_FIN] [date] NULL,
	[ACTIVO] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [CR].[T_CLIENTES]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CR].[T_CLIENTES](
	[id] [int] NOT NULL,
	[Primer_nombre] [varchar](50) NOT NULL,
	[Segundo_nombre] [varchar](50) NULL,
	[Primer_apellido] [varchar](50) NOT NULL,
	[Segundo_apellido] [varchar](50) NOT NULL,
	[Identificacion] [varchar](20) NOT NULL,
	[Fecha_nacimiento] [date] NOT NULL,
	[Genero] [varchar](1) NOT NULL,
	[Estado_civil] [varchar](50) NOT NULL,
	[CP] [varchar](5) NULL,
	[Direccion_domicilio] [varchar](200) NULL,
	[Provincia] [varchar](200) NULL,
	[Localidad] [varchar](200) NULL,
	[Cod_Tel_Pais] [varchar](2) NULL,
	[Telefono] [varchar](9) NULL,
	[Educacion] [varchar](100) NULL,
	[Oficio_laboral] [varchar](100) NULL,
	[email] [varchar](100) NULL,
	[Ingresos] [float] NULL,
	[Egresos] [float] NULL,
	[Saldo_promedio] [float] NULL,
	[N_tarjetas] [int] NULL,
	[credito_personal] [int] NULL,
	[credito_hipotecario] [int] NULL,
	[credito_en_mora] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[Identificacion] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [CR].[T_EFECTIVIDAD]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CR].[T_EFECTIVIDAD](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[idcampaña] [int] NOT NULL,
	[objtivo_efectividad] [decimal](18, 2) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [CR].[T_PROSPECTOS]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CR].[T_PROSPECTOS](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Nombre_completo] [varchar](203) NULL,
	[años] [int] NULL,
	[Ocupacion] [varchar](100) NULL,
	[Estado_civil] [varchar](50) NOT NULL,
	[educacion] [varchar](100) NULL,
	[credito_en_mora] [int] NULL,
	[saldo_promedio] [decimal](18, 2) NULL,
	[credito_personal] [int] NULL,
	[credito_hipotecario] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [CR].[T_REGISTROSCAMPAÑA]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CR].[T_REGISTROSCAMPAÑA](
	[ID] [int] NOT NULL,
	[ID2] [int] NOT NULL,
	[Nombre_completo] [varchar](203) NULL,
	[años] [int] NULL,
	[Ocupacion] [varchar](100) NULL,
	[Estado_civil] [varchar](50) NOT NULL,
	[educacion] [varchar](100) NULL,
	[credito_en_mora] [int] NULL,
	[saldo_promedio] [decimal](18, 2) NULL,
	[credito_personal] [int] NULL,
	[credito_hipotecario] [int] NULL,
	[CONTACT] [varchar](50) NULL,
	[MONTH] [varchar](50) NULL,
	[DAY_OF_WEEK] [varchar](50) NULL,
	[DURATION] [varchar](50) NULL,
	[CAMPAIGN] [varchar](50) NULL,
	[PDAYS] [varchar](50) NULL,
	[PREVIOUS] [varchar](50) NULL,
	[POUTCOME] [varchar](50) NULL,
	[EMP_VAR_ATE] [varchar](50) NULL,
	[CONS_PRICE_IDX] [varchar](50) NULL,
	[CONS_CONF_IDX] [varchar](50) NULL,
	[EURIBOR3M] [varchar](50) NULL,
	[NR_EMPLOYED] [varchar](50) NULL,
	[VAR_OBJ] [int] NULL,
	[CAMPAÑA] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [CR].[T_USUARIO]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CR].[T_USUARIO](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[usuario] [varchar](20) NOT NULL,
	[pass] [binary](64) NOT NULL,
	[primer_nombre] [varchar](50) NULL,
	[segundo_nombre] [varchar](50) NULL,
	[primer_apellido] [varchar](50) NULL,
	[segundo_apellido] [varchar](50) NULL,
	[id_legal] [varchar](15) NULL,
	[email] [varchar](200) NULL,
	[photo] [image] NULL,
	[Salt] [uniqueidentifier] NULL,
	[photocara] [image] NULL,
PRIMARY KEY CLUSTERED 
(
	[usuario] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [CR].[T_USUARIO_IMAGEN]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [CR].[T_USUARIO_IMAGEN](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[id_usuario] [varchar](20) NOT NULL,
	[imagen1] [image] NULL,
	[imagen2] [image] NULL,
	[imagen3] [image] NULL,
	[imagen4] [image] NULL,
	[imagen5] [image] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[error]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[error](
	[fecha] [date] NULL,
	[mensaje] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[importdatafull]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[importdatafull](
	[age] [varchar](50) NULL,
	[job] [varchar](50) NULL,
	[marital] [varchar](50) NULL,
	[education] [varchar](50) NULL,
	[default] [varchar](50) NULL,
	[housing] [varchar](50) NULL,
	[loan] [varchar](50) NULL,
	[contact] [varchar](50) NULL,
	[month] [varchar](50) NULL,
	[day_of_week] [varchar](50) NULL,
	[duration] [varchar](50) NULL,
	[campaign] [varchar](50) NULL,
	[pdays] [varchar](50) NULL,
	[previous] [varchar](50) NULL,
	[poutcome] [varchar](50) NULL,
	[emp var rate] [varchar](50) NULL,
	[cons price idx] [varchar](50) NULL,
	[cons conf idx] [varchar](50) NULL,
	[euribor3m] [varchar](50) NULL,
	[nr employed] [varchar](50) NULL,
	[var_obj ] [varchar](50) NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[error] ADD  DEFAULT (getdate()) FOR [fecha]
GO
/****** Object:  StoredProcedure [CR].[getuser]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE procedure [CR].[getuser] @user varchar(20)
  as
  select id,photo from CR.T_USUARIO where usuario = @user 
GO
/****** Object:  StoredProcedure [CR].[SP_ALLDATOS]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
  create procedure [CR].[SP_ALLDATOS]
  as
SELECT 
  A.ID
 ,A.ID AS ID2
 ,A.Nombre_completo 
 ,A.años
 ,A.Ocupacion
 ,A.Estado_civil
 ,A.educacion
 ,A.credito_en_mora
 ,A.saldo_promedio
 ,A.credito_personal
 ,A.credito_hipotecario
 ,B.CONTACT
 ,B.MONTH
 ,B.DAY_OF_WEEK
 ,B.DURATION
 ,B.CAMPAIGN
 ,B.PDAYS
 ,B.PREVIOUS
 ,B.POUTCOME
 ,B.[EMP VAR RATE] AS EMP_VAR_ATE
 ,B.[CONS PRICE IDX] AS [CONS_PRICE_IDX]
 ,B.[CONS CONF IDX] AS [CONS_CONF_IDX]
 ,B.EURIBOR3M 
 ,B.[NR EMPLOYED] AS [NR_EMPLOYED]
 ,NULL VAR_OBJ
 FROM CR.T_PROSPECTOS A
 LEFT JOIN CR.T_ATRIBUTOSCLIENTE B
 ON A.ID = B.ID	
GO
/****** Object:  StoredProcedure [CR].[SP_DELCLIENT]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create procedure [CR].[SP_DELCLIENT] @id int
  as
  delete from CR.T_PROSPECTOS where id=@id
GO
/****** Object:  StoredProcedure [CR].[SP_GETCLIENT]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
  CREATE procedure [CR].[SP_GETCLIENT]
  AS
  SET NOCOUNT ON
  TRUNCATE TABLE CR.T_PROSPECTOS

  INSERT INTO CR.T_PROSPECTOS
  SELECT 
   
  Primer_nombre+' '+Segundo_nombre+' '+Primer_apellido+' '+Segundo_apellido as Nombre_completo 
  ,round((datediff(MM,Fecha_nacimiento,GETDATE())/12), 0, 1) años
  ,Oficio_laboral as Ocupacion
  ,Estado_civil 
  ,educacion
  ,credito_en_mora
  ,cast(Saldo_promedio as decimal(18,2)) saldo_promedio
  ,credito_personal
  ,credito_hipotecario
  FROM CR.T_CLIENTES

  
  SELECT ID AS ID2,* FROM CR.T_PROSPECTOS
GO
/****** Object:  StoredProcedure [CR].[SP_GETCLIENT_FIL]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE procedure [CR].[SP_GETCLIENT_FIL] @edu varchar(100),@oficio varchar(100),@gen varchar(100),@estcivil varchar(100),@provincias varchar(100)
  AS
  SET NOCOUNT ON

  --declare @edu varchar(100)='Bachillerato',@oficio varchar(100)='',@gen varchar(100)='',@estcivil varchar(100)='',@provincias varchar(100)=''
  declare @sql varchar(max), @filtro varchar(max), @c int=0 
  
  --print @edu
  --print @oficio
  --print @gen
  --print @estcivil
  --print @provincias

  TRUNCATE TABLE CR.T_PROSPECTOS

    --select * FROM CR.T_CLIENTES where Oficio_laboral='Tecnico' and Genero='M' and Educacion='Bachillerato'


  set @sql = 
  'SELECT  
  Primer_nombre+'' ''+Segundo_nombre+'' ''+Primer_apellido+'' ''+Segundo_apellido as Nombre_completo 
  ,round((datediff(MM,Fecha_nacimiento,GETDATE())/12), 0, 1) años
  ,Oficio_laboral as Ocupacion
  ,Estado_civil 
  ,educacion
  ,credito_en_mora
  ,cast(Saldo_promedio as decimal(18,2)) saldo_promedio
  ,credito_personal
  ,credito_hipotecario
  FROM CR.T_CLIENTES 
  WHERE 
  id is not null 
  '
  set @sql = @sql + case when (@edu is null or @edu='' )   then '' else ' and educacion ='''+@edu+'''' end
  set @sql = @sql + case when (@oficio is null or @oficio='' ) then  '' else ' and Oficio_laboral ='''+@oficio+'''' end
  set @sql = @sql + case when (@gen is null or @gen='' ) then '' else ' and Genero ='''+@gen+'''' end
  set @sql = @sql + case when (@estcivil is null or @estcivil='' ) then '' else ' and Estado_civil ='''+@estcivil+'''' end
  set @sql = @sql + case when (@provincias is null or @provincias='' ) then '' else ' and Provincia ='''+@provincias+'''' end
							  
  --select @sql
  --select @sql
  
  INSERT INTO CR.T_PROSPECTOS
  exec (@sql)

    
  SELECT ID AS ID2,* FROM CR.T_PROSPECTOS
GO
/****** Object:  StoredProcedure [CR].[sp_insertphoto]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create procedure [CR].[sp_insertphoto] @user varchar(20), @photo image
as
insert into cr.T_USUARIO_IMAGEN(id_usuario,imagen1) values(@user,@photo)
GO
/****** Object:  StoredProcedure [CR].[SP_NEWCLIENT]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE procedure [CR].[SP_NEWCLIENT]
			       @Primer_nombre varchar(50)
				  ,@Segundo_nombre varchar(50)
				  ,@Primer_apellido varchar(50)
				  ,@Segundo_apellido varchar(50)
				  ,@Identificacion varchar(20) 
				  ,@Fecha_nacimiento varchar(20)
				  ,@Genero varchar(1) 
				  ,@Estado_civil varchar(50) 
				  ,@CP varchar(5)
				  ,@Direccion_domicilio varchar(200)
				  ,@Provincia varchar(200)
				  ,@Localidad varchar(200)
				  ,@Cod_Tel_Pais varchar(2)
				  ,@Telefono varchar(9)
				  ,@Educacion varchar(100)
				  ,@Oficio_laboral varchar(100)
				  ,@email varchar(100)
				  ,@Ingresos float
				  ,@Egresos float
				  ,@Saldo_promedio float
				  ,@N_tarjetas int
				  ,@credito_personal int
				  ,@credito_hipotecario int
				  ,@credito_en_mora int
				  as
SET NOCOUNT ON
declare @result varchar(max)
if not exists(select * from CR.T_CLIENTES where identificacion = @Identificacion)
begin
insert into CR.T_CLIENTES(Primer_nombre,Segundo_nombre,Primer_apellido,Segundo_apellido,
  Identificacion,Fecha_nacimiento,Genero,Estado_civil,CP,Direccion_domicilio,Provincia,
  Localidad,  Cod_Tel_Pais,  Telefono,  Educacion,  Oficio_laboral,  email,Ingresos,
  Egresos ,  Saldo_promedio ,  N_tarjetas ,  credito_personal ,  credito_hipotecario ,
  credito_en_mora ) values(@Primer_nombre
				  ,@Segundo_nombre
				  ,@Primer_apellido
				  ,@Segundo_apellido
				  ,@Identificacion
				  ,@Fecha_nacimiento
				  ,@Genero
				  ,@Estado_civil
				  ,@CP
				  ,@Direccion_domicilio
				  ,@Provincia 
				  ,@Localidad 
				  ,@Cod_Tel_Pais 
				  ,@Telefono 
				  ,@Educacion 
				  ,@Oficio_laboral 
				  ,@email
				  ,@Ingresos ,
				   @Egresos ,
				   @Saldo_promedio ,
				   @N_tarjetas ,
				   @credito_personal ,
				   @credito_hipotecario ,
				   @credito_en_mora 

				  )
select  '1' as rel
end
else 
begin
select '0' as rel
end

GO
/****** Object:  StoredProcedure [CR].[SP_selprospecto]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE procedure [CR].[SP_selprospecto]
  as
  select ID AS ID2,* from CR.T_PROSPECTOS
GO
/****** Object:  StoredProcedure [CR].[SPCAMPAÑAS]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create procedure [CR].[SPCAMPAÑAS]
AS
SELECT NOMBRE_CAMPAÑA FROM CR.T_CAMPANAS
GO
/****** Object:  StoredProcedure [CR].[SPGETREGISTROCAMPAÑA]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE procedure [CR].[SPGETREGISTROCAMPAÑA] @IDCAMPAÑA VARCHAR(100) AS
SELECT id, id2,Nombre_completo,años,Ocupacion,Estado_civil,educacion,credito_en_mora,saldo_promedio,credito_personal,credito_hipotecario,VAR_OBJ FROM  CR.T_REGISTROSCAMPAÑA WHERE CAMPAÑA IN (SELECT ID FROM CR.T_CAMPANAS WHERE NOMBRE_CAMPAÑA = @IDCAMPAÑA)
order by VAR_OBJ


--select *  FROM CR.T_PROSPECTOS A
GO
/****** Object:  StoredProcedure [CR].[SPGUARDARCAMPAÑA]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

--exec CR.SPGUARDARCAMPAÑA 'VENTAS SEGUROS COCHE'

CREATE procedure [CR].[SPGUARDARCAMPAÑA] @IDCAMPAÑA VARCHAR(100)
AS

SET NOCOUNT ON
--DECLARE @IDCAMPAÑA varchar(100)='VENTAS SEGUROS COCHE'

DELETE FROM CR.T_REGISTROSCAMPAÑA WHERE CAMPAÑA IN (SELECT ID FROM CR.T_CAMPANAS WHERE NOMBRE_CAMPAÑA = @IDCAMPAÑA)

INSERT INTO CR.T_REGISTROSCAMPAÑA
 SELECT 
  A.ID
 ,A.ID AS ID2
 ,A.Nombre_completo 
 ,A.años
 ,A.Ocupacion
 ,A.Estado_civil
 ,A.educacion
 ,A.credito_en_mora
 ,A.saldo_promedio
 ,A.credito_personal
 ,A.credito_hipotecario
 ,B.CONTACT
 ,B.MONTH
 ,B.DAY_OF_WEEK
 ,B.DURATION
 ,B.CAMPAIGN
 ,B.PDAYS
 ,B.PREVIOUS
 ,B.POUTCOME
 ,B.[EMP VAR RATE] AS EMP_VAR_ATE
 ,B.[CONS PRICE IDX] AS [CONS_PRICE_IDX]
 ,B.[CONS CONF IDX] AS [CONS_CONF_IDX]
 ,B.EURIBOR3M 
 ,B.[NR EMPLOYED] AS [NR_EMPLOYED]
 ,NULL VAR_OBJ
 ,(SELECT ID FROM CR.T_CAMPANAS WHERE NOMBRE_CAMPAÑA = @IDCAMPAÑA) AS CAMPAÑA
 --INTO CR.T_REGISTROSCAMPAÑA
 FROM CR.T_PROSPECTOS A
 LEFT JOIN CR.T_ATRIBUTOSCLIENTE B
 ON A.ID = B.ID	


 SELECT  * FROM CR.T_REGISTROSCAMPAÑA

--truncate table CR.T_REGISTROSCAMPAÑA5

 --alter procedure CR.SPUPDATEOBJ @id varchar(6),@varobj varchar(1)
 --as
 --set @id = cast(@id as int)
 --set @varobj = cast(@varobj as int)

 --update CR.T_REGISTROSCAMPAÑA set var_obj = @varobj where id=@id

 --sp_who2
GO
/****** Object:  StoredProcedure [CR].[SPGUARDARCAMPAÑANEW]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE procedure [CR].[SPGUARDARCAMPAÑANEW] @nombre varchar(100),@fechaini varchar(10),@fechafin varchar(10), @activo int
  as
  SET NOCOUNT ON
  if exists(select * from [TFM].[CR].[T_CAMPANAS]  where NOMBRE_CAMPAÑA = @nombre)
	begin
	select 'Campaña existente'
	end
  else
  begin 
  insert into [CR].[T_CAMPANAS](NOMBRE_CAMPAÑA,FECHA_INI,FECHA_FIN,ACTIVO) values(@nombre,@fechaini,@fechafin,@activo)
  select 'Campaña Guardada'
  end
  
GO
/****** Object:  StoredProcedure [CR].[SPUPDATEOBJ]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
 CREATE procedure [CR].[SPUPDATEOBJ] @id varchar(6),@varobj varchar(1)
 as
 set @id = cast(@id as int)
 set @varobj = cast(@varobj as int)

 update CR.T_REGISTROSCAMPAÑA set var_obj = @varobj where id=@id
GO
/****** Object:  StoredProcedure [CR].[uspAddUser]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [CR].[uspAddUser]
    @pLogin VARCHAR(20), 
    @pPassword VARCHAR(50),
    @primer_nombre VARCHAR(50) , 
    @primer_apellido VARCHAR(50) ,
	@segundo_nombre VARCHAR(50) ,
	@segundo_apellido VARCHAR(50) ,
	@email varchar(200) ,
	@photo image,
	--@photocara image,
	@dni varchar(15)
	--@responseMessage VARCHAR(250) output

AS
BEGIN
    SET NOCOUNT ON

    DECLARE @salt UNIQUEIDENTIFIER=NEWID(),@responseMessage VARCHAR(250)

    BEGIN TRY

        INSERT INTO CR.T_USUARIO (usuario, pass, Salt, primer_nombre,segundo_nombre, primer_apellido,segundo_apellido,id_legal,email,photo)
        VALUES(@pLogin, HASHBYTES('MD5', @pPassword+CAST(@salt AS VARCHAR(max))), @salt, @primer_nombre, @segundo_nombre,@primer_apellido,@segundo_apellido,@dni,@email,@photo)

       SET @responseMessage='Registro Guardado Exitosamente'

    END TRY
    BEGIN CATCH
        --insert into dbo.error(mensaje) values(ERROR_MESSAGE())
		SET @responseMessage=cast(ERROR_MESSAGE() as varchar(max))
    END CATCH
	select @responseMessage
END


--create table dbo.error
--(
--fecha date default getdate()
--,mensaje varchar(max)
--)

--select * from dbo.error
--select * from CR.T_USUARIO
--truncate table CR.T_USUARIO

GO
/****** Object:  StoredProcedure [CR].[uspLogin]    Script Date: 15/09/2021 22:23:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [CR].[uspLogin]
    @pLoginName NVARCHAR(254),
    @pPassword NVARCHAR(50),
    @responseMessage NVARCHAR(250)='' OUTPUT
AS
BEGIN

    SET NOCOUNT ON

    DECLARE @userID INT

    IF EXISTS (SELECT TOP 1 id FROM CR.T_USUARIO WHERE usuario=@pLoginName)
    BEGIN
        SET @userID=(SELECT id FROM CR.T_USUARIO WHERE usuario=@pLoginName AND Pass=HASHBYTES('MD5', @pPassword+CAST(Salt AS NVARCHAR(36))))

       IF(@userID IS NULL)
           SET @responseMessage='Incorrect password'
       ELSE 
           SET @responseMessage='User successfully logged in'
    END
    ELSE
       SET @responseMessage='Invalid login'

END
GO
USE [master]
GO
ALTER DATABASE [TFM] SET  READ_WRITE 
GO
