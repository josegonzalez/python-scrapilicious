CREATE TABLE `bookmarks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hash` varchar(64) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `title` text,
  `link` text,
  `bookmarks` int(11) DEFAULT NULL,
  `tags` text,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_user_link` (`hash`,`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;