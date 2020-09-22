-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-09-2020 a las 22:33:43
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `politica`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acusacion`
--

CREATE TABLE `acusacion` (
  `fk_caso` int(11) NOT NULL,
  `fk_imputado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `acusacion`
--

INSERT INTO `acusacion` (`fk_caso`, `fk_imputado`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargos`
--

CREATE TABLE `cargos` (
  `id_cargo` int(11) NOT NULL,
  `cargo` varchar(50) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `cargos`
--

INSERT INTO `cargos` (`id_cargo`, `cargo`) VALUES
(1, 'Militante');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `casos`
--

CREATE TABLE `casos` (
  `id_caso` int(11) NOT NULL,
  `credencial` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `montante` decimal(20,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `casos`
--

INSERT INTO `casos` (`id_caso`, `credencial`, `montante`) VALUES
(1, 'X28JH2015K', '200000.00'),
(2, 'GF444', '75555.55');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `imputados`
--

CREATE TABLE `imputados` (
  `id_imputado` int(11) NOT NULL,
  `nombre` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `apellidos` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `fk_partido` int(11) NOT NULL,
  `fk_cargo` int(11) NOT NULL,
  `grupoRH` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `nacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `imputados`
--

INSERT INTO `imputados` (`id_imputado`, `nombre`, `apellidos`, `fk_partido`, `fk_cargo`, `grupoRH`, `nacimiento`) VALUES
(1, 'Antonio Juan', 'Tarazona Lledó', 1, 1, 'AB+', '1960-09-06');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partidos`
--

CREATE TABLE `partidos` (
  `id_partido` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `siglas` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `logo` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `partidos`
--

INSERT INTO `partidos` (`id_partido`, `nombre`, `siglas`, `logo`) VALUES
(1, 'Partido Popular', 'PP', 'C:/x-python/02Grafico/03Corrupcion/imagenes/logoPP.jpeg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `usuario` varchar(25) COLLATE utf8_spanish_ci NOT NULL,
  `password` varchar(25) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `usuario`, `password`) VALUES
(1, 'administrador', '123123');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `acusacion`
--
ALTER TABLE `acusacion`
  ADD PRIMARY KEY (`fk_caso`,`fk_imputado`),
  ADD KEY `fk_imputado` (`fk_imputado`);

--
-- Indices de la tabla `cargos`
--
ALTER TABLE `cargos`
  ADD PRIMARY KEY (`id_cargo`),
  ADD UNIQUE KEY `idx_cargo` (`cargo`);

--
-- Indices de la tabla `casos`
--
ALTER TABLE `casos`
  ADD PRIMARY KEY (`id_caso`),
  ADD UNIQUE KEY `idx_credencial` (`credencial`);

--
-- Indices de la tabla `imputados`
--
ALTER TABLE `imputados`
  ADD PRIMARY KEY (`id_imputado`),
  ADD UNIQUE KEY `fk_partido` (`fk_partido`),
  ADD UNIQUE KEY `fk_cargo` (`fk_cargo`);

--
-- Indices de la tabla `partidos`
--
ALTER TABLE `partidos`
  ADD PRIMARY KEY (`id_partido`),
  ADD UNIQUE KEY `idx_nombre` (`nombre`) USING BTREE,
  ADD UNIQUE KEY `idx_siglas` (`siglas`) USING BTREE;

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `usuario` (`usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cargos`
--
ALTER TABLE `cargos`
  MODIFY `id_cargo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `casos`
--
ALTER TABLE `casos`
  MODIFY `id_caso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `imputados`
--
ALTER TABLE `imputados`
  MODIFY `id_imputado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `partidos`
--
ALTER TABLE `partidos`
  MODIFY `id_partido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `acusacion`
--
ALTER TABLE `acusacion`
  ADD CONSTRAINT `acusacion_ibfk_1` FOREIGN KEY (`fk_imputado`) REFERENCES `imputados` (`id_imputado`),
  ADD CONSTRAINT `acusacion_ibfk_2` FOREIGN KEY (`fk_caso`) REFERENCES `casos` (`id_caso`);

--
-- Filtros para la tabla `imputados`
--
ALTER TABLE `imputados`
  ADD CONSTRAINT `imputados_ibfk_1` FOREIGN KEY (`fk_partido`) REFERENCES `partidos` (`id_partido`),
  ADD CONSTRAINT `imputados_ibfk_2` FOREIGN KEY (`fk_cargo`) REFERENCES `cargos` (`id_cargo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
