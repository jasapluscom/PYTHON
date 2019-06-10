SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
--
-- Database: `pymysql1`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `title` tinytext NOT NULL,
  `author` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `books` (`id`, `title`, `author`) VALUES
(1, 'Good to Great', 'Jim Collins'),
(2, 'Juniper Lemon\'s Happiness Index', 'Julie Israel'),
(3, 'The Summer Of Impossible Things', 'By Rowan Coleman');

CREATE TABLE `movies` (
  `id` int(11) NOT NULL,
  `title` tinytext NOT NULL,
  `category` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `movies` (`id`, `title`, `category`) VALUES
(1, 'Captain Marvel', 'action'),
(2, 'X-men', 'action');

ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `movies`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

ALTER TABLE `movies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;COMMIT;


