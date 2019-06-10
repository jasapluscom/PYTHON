SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `page` (
  `id` int(11) NOT NULL,
  `header` text NOT NULL,
  `container` text NOT NULL,
  `mode` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `page` (`id`, `header`, `container`, `mode`) VALUES
(1, 'About Ringlayer', 'I\'m a roboticist based in Indonesia.\r\nmy expertises are : robotic, programming, digital electronic, computer vision and artificial intelligence (machine learning for robotic).\r\n<br>\r\nThis site was developed using python3 and flask, source code can be cloned from github.\r\n<br>\r\ngithub:\r\n<br>\r\n<a href=\"https://github.com/ringlayer\">https://github.com/ringlayer</a>\r\n<br>\r\nIf you wish to become one of my friend, you can follow me on twitter : <a href=https://www.twitter.com/ringlayer>@ringlayer</a>.\r\n<br>\r\nAll right ! Hopefully you didn\'t think this site as a ludicrous site..Have a nice day buddy !\r\n', 'about'),
(2, 'Contact Me', 'Contact Me on Github : @ringlayer\r\n<br>\r\nThank you \r\n<br>\r\n<i>Mr Ringlayer</i>\r\n', 'kontak'),
(3, 'Portfolio', '<b>Portfolio page coming soon !!!</b>', 'portfolios');

ALTER TABLE `page`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `page`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;COMMIT;

