<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'shaheer_db' );

/** MySQL database username */
define( 'DB_USER', 'root' );

/** MySQL database password */
define( 'DB_PASSWORD', '' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'vDZ{PlLo5<W|ZpI}}||j`rK7D~Dz=_/g)@>eTxv&?[@g2bF4f+]76y!@7{<.dpBW' );
define( 'SECURE_AUTH_KEY',  '&SZ9+ ie+Tm1oZH{QAggU=ol>UbT$LJImnXRtGw>`W<gb@pVKQ,!6O!f vm(t[~!' );
define( 'LOGGED_IN_KEY',    'LD1t_)X3]j1h:%BSW[eHdX)`9h=#Qv/O|7;w29-mPIo>0| C6EWz>-GxR9Q7AqWY' );
define( 'NONCE_KEY',        'kEM%08z7zq<~cpH[GL7-YG9KGS)Bc0?l)NF,Bpq?3|oT)%:l.$d<CdD<ziC b1%i' );
define( 'AUTH_SALT',        'D46NO5#5>0PX)3[N#~]Rnc166aZG{Rftjqbqnz/yz`6zT_0NjEz>1|)&n!-`r~<z' );
define( 'SECURE_AUTH_SALT', 'W#-y._kvh_J@DTl^Rg~dd[mmMECS)yz.WU(Oia4[0Zk%xS*fG+gB%3a_%h0bK1EM' );
define( 'LOGGED_IN_SALT',   'lg<<`$rFsQD9ryYE,dtb(1)rL&>q<j_=p1p4EL+*JbRx! BNV~/IV`,:-^}Gf%W0' );
define( 'NONCE_SALT',       'YrI^XJ7ir.`_awCk0ssyzy`,P>PpS/1xOB7_=r$YG-4K_#Mqay&!6`$v8{>!81V,' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
