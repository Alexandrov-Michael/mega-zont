#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# manage.py dumpscript

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import utc

def run():
    from django.contrib.auth.models import Permission

    auth_permission_1 = Permission()
    auth_permission_1.name = u'Can add log entry'
    auth_permission_1.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_1.codename = u'add_logentry'
    auth_permission_1.save()

    auth_permission_2 = Permission()
    auth_permission_2.name = u'Can change log entry'
    auth_permission_2.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_2.codename = u'change_logentry'
    auth_permission_2.save()

    auth_permission_3 = Permission()
    auth_permission_3.name = u'Can delete log entry'
    auth_permission_3.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_3.codename = u'delete_logentry'
    auth_permission_3.save()

    auth_permission_4 = Permission()
    auth_permission_4.name = u'Can add group'
    auth_permission_4.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_4.codename = u'add_group'
    auth_permission_4.save()

    auth_permission_5 = Permission()
    auth_permission_5.name = u'Can change group'
    auth_permission_5.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_5.codename = u'change_group'
    auth_permission_5.save()

    auth_permission_6 = Permission()
    auth_permission_6.name = u'Can delete group'
    auth_permission_6.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_6.codename = u'delete_group'
    auth_permission_6.save()

    auth_permission_7 = Permission()
    auth_permission_7.name = u'Can add permission'
    auth_permission_7.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_7.codename = u'add_permission'
    auth_permission_7.save()

    auth_permission_8 = Permission()
    auth_permission_8.name = u'Can change permission'
    auth_permission_8.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_8.codename = u'change_permission'
    auth_permission_8.save()

    auth_permission_9 = Permission()
    auth_permission_9.name = u'Can delete permission'
    auth_permission_9.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_9.codename = u'delete_permission'
    auth_permission_9.save()

    auth_permission_10 = Permission()
    auth_permission_10.name = u'Can add user'
    auth_permission_10.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_10.codename = u'add_user'
    auth_permission_10.save()

    auth_permission_11 = Permission()
    auth_permission_11.name = u'Can change user'
    auth_permission_11.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_11.codename = u'change_user'
    auth_permission_11.save()

    auth_permission_12 = Permission()
    auth_permission_12.name = u'Can delete user'
    auth_permission_12.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_12.codename = u'delete_user'
    auth_permission_12.save()

    auth_permission_13 = Permission()
    auth_permission_13.name = u'Can add \u0427\u0438\u0441\u0442\u044b\u0439 html'
    auth_permission_13.content_type = ContentType.objects.get(app_label="bootstrap_tags", model="clearhtml")
    auth_permission_13.codename = u'add_clearhtml'
    auth_permission_13.save()

    auth_permission_14 = Permission()
    auth_permission_14.name = u'Can change \u0427\u0438\u0441\u0442\u044b\u0439 html'
    auth_permission_14.content_type = ContentType.objects.get(app_label="bootstrap_tags", model="clearhtml")
    auth_permission_14.codename = u'change_clearhtml'
    auth_permission_14.save()

    auth_permission_15 = Permission()
    auth_permission_15.name = u'Can delete \u0427\u0438\u0441\u0442\u044b\u0439 html'
    auth_permission_15.content_type = ContentType.objects.get(app_label="bootstrap_tags", model="clearhtml")
    auth_permission_15.codename = u'delete_clearhtml'
    auth_permission_15.save()

    auth_permission_16 = Permission()
    auth_permission_16.name = u'Can add cms plugin'
    auth_permission_16.content_type = ContentType.objects.get(app_label="cms", model="cmsplugin")
    auth_permission_16.codename = u'add_cmsplugin'
    auth_permission_16.save()

    auth_permission_17 = Permission()
    auth_permission_17.name = u'Can change cms plugin'
    auth_permission_17.content_type = ContentType.objects.get(app_label="cms", model="cmsplugin")
    auth_permission_17.codename = u'change_cmsplugin'
    auth_permission_17.save()

    auth_permission_18 = Permission()
    auth_permission_18.name = u'Can delete cms plugin'
    auth_permission_18.content_type = ContentType.objects.get(app_label="cms", model="cmsplugin")
    auth_permission_18.codename = u'delete_cmsplugin'
    auth_permission_18.save()

    auth_permission_19 = Permission()
    auth_permission_19.name = u'Can add Page global permission'
    auth_permission_19.content_type = ContentType.objects.get(app_label="cms", model="globalpagepermission")
    auth_permission_19.codename = u'add_globalpagepermission'
    auth_permission_19.save()

    auth_permission_20 = Permission()
    auth_permission_20.name = u'Can change Page global permission'
    auth_permission_20.content_type = ContentType.objects.get(app_label="cms", model="globalpagepermission")
    auth_permission_20.codename = u'change_globalpagepermission'
    auth_permission_20.save()

    auth_permission_21 = Permission()
    auth_permission_21.name = u'Can delete Page global permission'
    auth_permission_21.content_type = ContentType.objects.get(app_label="cms", model="globalpagepermission")
    auth_permission_21.codename = u'delete_globalpagepermission'
    auth_permission_21.save()

    auth_permission_22 = Permission()
    auth_permission_22.name = u'Can add page'
    auth_permission_22.content_type = ContentType.objects.get(app_label="cms", model="page")
    auth_permission_22.codename = u'add_page'
    auth_permission_22.save()

    auth_permission_23 = Permission()
    auth_permission_23.name = u'Can change page'
    auth_permission_23.content_type = ContentType.objects.get(app_label="cms", model="page")
    auth_permission_23.codename = u'change_page'
    auth_permission_23.save()

    auth_permission_24 = Permission()
    auth_permission_24.name = u'Can delete page'
    auth_permission_24.content_type = ContentType.objects.get(app_label="cms", model="page")
    auth_permission_24.codename = u'delete_page'
    auth_permission_24.save()

    auth_permission_25 = Permission()
    auth_permission_25.name = u'Can view page'
    auth_permission_25.content_type = ContentType.objects.get(app_label="cms", model="page")
    auth_permission_25.codename = u'view_page'
    auth_permission_25.save()

    auth_permission_26 = Permission()
    auth_permission_26.name = u'Can add PageModerator'
    auth_permission_26.content_type = ContentType.objects.get(app_label="cms", model="pagemoderator")
    auth_permission_26.codename = u'add_pagemoderator'
    auth_permission_26.save()

    auth_permission_27 = Permission()
    auth_permission_27.name = u'Can change PageModerator'
    auth_permission_27.content_type = ContentType.objects.get(app_label="cms", model="pagemoderator")
    auth_permission_27.codename = u'change_pagemoderator'
    auth_permission_27.save()

    auth_permission_28 = Permission()
    auth_permission_28.name = u'Can delete PageModerator'
    auth_permission_28.content_type = ContentType.objects.get(app_label="cms", model="pagemoderator")
    auth_permission_28.codename = u'delete_pagemoderator'
    auth_permission_28.save()

    auth_permission_29 = Permission()
    auth_permission_29.name = u'Can add Page moderator state'
    auth_permission_29.content_type = ContentType.objects.get(app_label="cms", model="pagemoderatorstate")
    auth_permission_29.codename = u'add_pagemoderatorstate'
    auth_permission_29.save()

    auth_permission_30 = Permission()
    auth_permission_30.name = u'Can change Page moderator state'
    auth_permission_30.content_type = ContentType.objects.get(app_label="cms", model="pagemoderatorstate")
    auth_permission_30.codename = u'change_pagemoderatorstate'
    auth_permission_30.save()

    auth_permission_31 = Permission()
    auth_permission_31.name = u'Can delete Page moderator state'
    auth_permission_31.content_type = ContentType.objects.get(app_label="cms", model="pagemoderatorstate")
    auth_permission_31.codename = u'delete_pagemoderatorstate'
    auth_permission_31.save()

    auth_permission_32 = Permission()
    auth_permission_32.name = u'Can add Page permission'
    auth_permission_32.content_type = ContentType.objects.get(app_label="cms", model="pagepermission")
    auth_permission_32.codename = u'add_pagepermission'
    auth_permission_32.save()

    auth_permission_33 = Permission()
    auth_permission_33.name = u'Can change Page permission'
    auth_permission_33.content_type = ContentType.objects.get(app_label="cms", model="pagepermission")
    auth_permission_33.codename = u'change_pagepermission'
    auth_permission_33.save()

    auth_permission_34 = Permission()
    auth_permission_34.name = u'Can delete Page permission'
    auth_permission_34.content_type = ContentType.objects.get(app_label="cms", model="pagepermission")
    auth_permission_34.codename = u'delete_pagepermission'
    auth_permission_34.save()

    auth_permission_35 = Permission()
    auth_permission_35.name = u'Can add User (page)'
    auth_permission_35.content_type = ContentType.objects.get(app_label="cms", model="pageuser")
    auth_permission_35.codename = u'add_pageuser'
    auth_permission_35.save()

    auth_permission_36 = Permission()
    auth_permission_36.name = u'Can change User (page)'
    auth_permission_36.content_type = ContentType.objects.get(app_label="cms", model="pageuser")
    auth_permission_36.codename = u'change_pageuser'
    auth_permission_36.save()

    auth_permission_37 = Permission()
    auth_permission_37.name = u'Can delete User (page)'
    auth_permission_37.content_type = ContentType.objects.get(app_label="cms", model="pageuser")
    auth_permission_37.codename = u'delete_pageuser'
    auth_permission_37.save()

    auth_permission_38 = Permission()
    auth_permission_38.name = u'Can add User group (page)'
    auth_permission_38.content_type = ContentType.objects.get(app_label="cms", model="pageusergroup")
    auth_permission_38.codename = u'add_pageusergroup'
    auth_permission_38.save()

    auth_permission_39 = Permission()
    auth_permission_39.name = u'Can change User group (page)'
    auth_permission_39.content_type = ContentType.objects.get(app_label="cms", model="pageusergroup")
    auth_permission_39.codename = u'change_pageusergroup'
    auth_permission_39.save()

    auth_permission_40 = Permission()
    auth_permission_40.name = u'Can delete User group (page)'
    auth_permission_40.content_type = ContentType.objects.get(app_label="cms", model="pageusergroup")
    auth_permission_40.codename = u'delete_pageusergroup'
    auth_permission_40.save()

    auth_permission_41 = Permission()
    auth_permission_41.name = u'Can add placeholder'
    auth_permission_41.content_type = ContentType.objects.get(app_label="cms", model="placeholder")
    auth_permission_41.codename = u'add_placeholder'
    auth_permission_41.save()

    auth_permission_42 = Permission()
    auth_permission_42.name = u'Can change placeholder'
    auth_permission_42.content_type = ContentType.objects.get(app_label="cms", model="placeholder")
    auth_permission_42.codename = u'change_placeholder'
    auth_permission_42.save()

    auth_permission_43 = Permission()
    auth_permission_43.name = u'Can delete placeholder'
    auth_permission_43.content_type = ContentType.objects.get(app_label="cms", model="placeholder")
    auth_permission_43.codename = u'delete_placeholder'
    auth_permission_43.save()

    auth_permission_44 = Permission()
    auth_permission_44.name = u'Can add title'
    auth_permission_44.content_type = ContentType.objects.get(app_label="cms", model="title")
    auth_permission_44.codename = u'add_title'
    auth_permission_44.save()

    auth_permission_45 = Permission()
    auth_permission_45.name = u'Can change title'
    auth_permission_45.content_type = ContentType.objects.get(app_label="cms", model="title")
    auth_permission_45.codename = u'change_title'
    auth_permission_45.save()

    auth_permission_46 = Permission()
    auth_permission_46.name = u'Can delete title'
    auth_permission_46.content_type = ContentType.objects.get(app_label="cms", model="title")
    auth_permission_46.codename = u'delete_title'
    auth_permission_46.save()

    auth_permission_47 = Permission()
    auth_permission_47.name = u'Can add slider plugin'
    auth_permission_47.content_type = ContentType.objects.get(app_label="cmsplugin_nivoslider", model="sliderplugin")
    auth_permission_47.codename = u'add_sliderplugin'
    auth_permission_47.save()

    auth_permission_48 = Permission()
    auth_permission_48.name = u'Can change slider plugin'
    auth_permission_48.content_type = ContentType.objects.get(app_label="cmsplugin_nivoslider", model="sliderplugin")
    auth_permission_48.codename = u'change_sliderplugin'
    auth_permission_48.save()

    auth_permission_49 = Permission()
    auth_permission_49.name = u'Can delete slider plugin'
    auth_permission_49.content_type = ContentType.objects.get(app_label="cmsplugin_nivoslider", model="sliderplugin")
    auth_permission_49.codename = u'delete_sliderplugin'
    auth_permission_49.save()

    auth_permission_50 = Permission()
    auth_permission_50.name = u'Can add content type'
    auth_permission_50.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_50.codename = u'add_contenttype'
    auth_permission_50.save()

    auth_permission_51 = Permission()
    auth_permission_51.name = u'Can change content type'
    auth_permission_51.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_51.codename = u'change_contenttype'
    auth_permission_51.save()

    auth_permission_52 = Permission()
    auth_permission_52.name = u'Can delete content type'
    auth_permission_52.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_52.codename = u'delete_contenttype'
    auth_permission_52.save()

    auth_permission_53 = Permission()
    auth_permission_53.name = u'Can add dashboard preferences'
    auth_permission_53.content_type = ContentType.objects.get(app_label="dashboard", model="dashboardpreferences")
    auth_permission_53.codename = u'add_dashboardpreferences'
    auth_permission_53.save()

    auth_permission_54 = Permission()
    auth_permission_54.name = u'Can change dashboard preferences'
    auth_permission_54.content_type = ContentType.objects.get(app_label="dashboard", model="dashboardpreferences")
    auth_permission_54.codename = u'change_dashboardpreferences'
    auth_permission_54.save()

    auth_permission_55 = Permission()
    auth_permission_55.name = u'Can delete dashboard preferences'
    auth_permission_55.content_type = ContentType.objects.get(app_label="dashboard", model="dashboardpreferences")
    auth_permission_55.codename = u'delete_dashboardpreferences'
    auth_permission_55.save()

    auth_permission_56 = Permission()
    auth_permission_56.name = u'Can add source'
    auth_permission_56.content_type = ContentType.objects.get(app_label="easy_thumbnails", model="source")
    auth_permission_56.codename = u'add_source'
    auth_permission_56.save()

    auth_permission_57 = Permission()
    auth_permission_57.name = u'Can change source'
    auth_permission_57.content_type = ContentType.objects.get(app_label="easy_thumbnails", model="source")
    auth_permission_57.codename = u'change_source'
    auth_permission_57.save()

    auth_permission_58 = Permission()
    auth_permission_58.name = u'Can delete source'
    auth_permission_58.content_type = ContentType.objects.get(app_label="easy_thumbnails", model="source")
    auth_permission_58.codename = u'delete_source'
    auth_permission_58.save()

    auth_permission_59 = Permission()
    auth_permission_59.name = u'Can add thumbnail'
    auth_permission_59.content_type = ContentType.objects.get(app_label="easy_thumbnails", model="thumbnail")
    auth_permission_59.codename = u'add_thumbnail'
    auth_permission_59.save()

    auth_permission_60 = Permission()
    auth_permission_60.name = u'Can change thumbnail'
    auth_permission_60.content_type = ContentType.objects.get(app_label="easy_thumbnails", model="thumbnail")
    auth_permission_60.codename = u'change_thumbnail'
    auth_permission_60.save()

    auth_permission_61 = Permission()
    auth_permission_61.name = u'Can delete thumbnail'
    auth_permission_61.content_type = ContentType.objects.get(app_label="easy_thumbnails", model="thumbnail")
    auth_permission_61.codename = u'delete_thumbnail'
    auth_permission_61.save()

    auth_permission_62 = Permission()
    auth_permission_62.name = u'Can add clipboard'
    auth_permission_62.content_type = ContentType.objects.get(app_label="filer", model="clipboard")
    auth_permission_62.codename = u'add_clipboard'
    auth_permission_62.save()

    auth_permission_63 = Permission()
    auth_permission_63.name = u'Can change clipboard'
    auth_permission_63.content_type = ContentType.objects.get(app_label="filer", model="clipboard")
    auth_permission_63.codename = u'change_clipboard'
    auth_permission_63.save()

    auth_permission_64 = Permission()
    auth_permission_64.name = u'Can delete clipboard'
    auth_permission_64.content_type = ContentType.objects.get(app_label="filer", model="clipboard")
    auth_permission_64.codename = u'delete_clipboard'
    auth_permission_64.save()

    auth_permission_65 = Permission()
    auth_permission_65.name = u'Can add clipboard item'
    auth_permission_65.content_type = ContentType.objects.get(app_label="filer", model="clipboarditem")
    auth_permission_65.codename = u'add_clipboarditem'
    auth_permission_65.save()

    auth_permission_66 = Permission()
    auth_permission_66.name = u'Can change clipboard item'
    auth_permission_66.content_type = ContentType.objects.get(app_label="filer", model="clipboarditem")
    auth_permission_66.codename = u'change_clipboarditem'
    auth_permission_66.save()

    auth_permission_67 = Permission()
    auth_permission_67.name = u'Can delete clipboard item'
    auth_permission_67.content_type = ContentType.objects.get(app_label="filer", model="clipboarditem")
    auth_permission_67.codename = u'delete_clipboarditem'
    auth_permission_67.save()

    auth_permission_68 = Permission()
    auth_permission_68.name = u'Can add file'
    auth_permission_68.content_type = ContentType.objects.get(app_label="filer", model="file")
    auth_permission_68.codename = u'add_file'
    auth_permission_68.save()

    auth_permission_69 = Permission()
    auth_permission_69.name = u'Can change file'
    auth_permission_69.content_type = ContentType.objects.get(app_label="filer", model="file")
    auth_permission_69.codename = u'change_file'
    auth_permission_69.save()

    auth_permission_70 = Permission()
    auth_permission_70.name = u'Can delete file'
    auth_permission_70.content_type = ContentType.objects.get(app_label="filer", model="file")
    auth_permission_70.codename = u'delete_file'
    auth_permission_70.save()

    auth_permission_71 = Permission()
    auth_permission_71.name = u'Can add Folder'
    auth_permission_71.content_type = ContentType.objects.get(app_label="filer", model="folder")
    auth_permission_71.codename = u'add_folder'
    auth_permission_71.save()

    auth_permission_72 = Permission()
    auth_permission_72.name = u'Can use directory listing'
    auth_permission_72.content_type = ContentType.objects.get(app_label="filer", model="folder")
    auth_permission_72.codename = u'can_use_directory_listing'
    auth_permission_72.save()

    auth_permission_73 = Permission()
    auth_permission_73.name = u'Can change Folder'
    auth_permission_73.content_type = ContentType.objects.get(app_label="filer", model="folder")
    auth_permission_73.codename = u'change_folder'
    auth_permission_73.save()

    auth_permission_74 = Permission()
    auth_permission_74.name = u'Can delete Folder'
    auth_permission_74.content_type = ContentType.objects.get(app_label="filer", model="folder")
    auth_permission_74.codename = u'delete_folder'
    auth_permission_74.save()

    auth_permission_75 = Permission()
    auth_permission_75.name = u'Can add folder permission'
    auth_permission_75.content_type = ContentType.objects.get(app_label="filer", model="folderpermission")
    auth_permission_75.codename = u'add_folderpermission'
    auth_permission_75.save()

    auth_permission_76 = Permission()
    auth_permission_76.name = u'Can change folder permission'
    auth_permission_76.content_type = ContentType.objects.get(app_label="filer", model="folderpermission")
    auth_permission_76.codename = u'change_folderpermission'
    auth_permission_76.save()

    auth_permission_77 = Permission()
    auth_permission_77.name = u'Can delete folder permission'
    auth_permission_77.content_type = ContentType.objects.get(app_label="filer", model="folderpermission")
    auth_permission_77.codename = u'delete_folderpermission'
    auth_permission_77.save()

    auth_permission_78 = Permission()
    auth_permission_78.name = u'Can add image'
    auth_permission_78.content_type = ContentType.objects.get(app_label="filer", model="image")
    auth_permission_78.codename = u'add_image'
    auth_permission_78.save()

    auth_permission_79 = Permission()
    auth_permission_79.name = u'Can change image'
    auth_permission_79.content_type = ContentType.objects.get(app_label="filer", model="image")
    auth_permission_79.codename = u'change_image'
    auth_permission_79.save()

    auth_permission_80 = Permission()
    auth_permission_80.name = u'Can delete image'
    auth_permission_80.content_type = ContentType.objects.get(app_label="filer", model="image")
    auth_permission_80.codename = u'delete_image'
    auth_permission_80.save()

    auth_permission_81 = Permission()
    auth_permission_81.name = u'Can add bookmark'
    auth_permission_81.content_type = ContentType.objects.get(app_label="menu", model="bookmark")
    auth_permission_81.codename = u'add_bookmark'
    auth_permission_81.save()

    auth_permission_82 = Permission()
    auth_permission_82.name = u'Can change bookmark'
    auth_permission_82.content_type = ContentType.objects.get(app_label="menu", model="bookmark")
    auth_permission_82.codename = u'change_bookmark'
    auth_permission_82.save()

    auth_permission_83 = Permission()
    auth_permission_83.name = u'Can delete bookmark'
    auth_permission_83.content_type = ContentType.objects.get(app_label="menu", model="bookmark")
    auth_permission_83.codename = u'delete_bookmark'
    auth_permission_83.save()

    auth_permission_84 = Permission()
    auth_permission_84.name = u'Can add cache key'
    auth_permission_84.content_type = ContentType.objects.get(app_label="menus", model="cachekey")
    auth_permission_84.codename = u'add_cachekey'
    auth_permission_84.save()

    auth_permission_85 = Permission()
    auth_permission_85.name = u'Can change cache key'
    auth_permission_85.content_type = ContentType.objects.get(app_label="menus", model="cachekey")
    auth_permission_85.codename = u'change_cachekey'
    auth_permission_85.save()

    auth_permission_86 = Permission()
    auth_permission_86.name = u'Can delete cache key'
    auth_permission_86.content_type = ContentType.objects.get(app_label="menus", model="cachekey")
    auth_permission_86.codename = u'delete_cachekey'
    auth_permission_86.save()

    auth_permission_87 = Permission()
    auth_permission_87.name = u'Can add form log'
    auth_permission_87.content_type = ContentType.objects.get(app_label="myforms", model="formlog")
    auth_permission_87.codename = u'add_formlog'
    auth_permission_87.save()

    auth_permission_88 = Permission()
    auth_permission_88.name = u'Can change form log'
    auth_permission_88.content_type = ContentType.objects.get(app_label="myforms", model="formlog")
    auth_permission_88.codename = u'change_formlog'
    auth_permission_88.save()

    auth_permission_89 = Permission()
    auth_permission_89.name = u'Can delete form log'
    auth_permission_89.content_type = ContentType.objects.get(app_label="myforms", model="formlog")
    auth_permission_89.codename = u'delete_formlog'
    auth_permission_89.save()

    auth_permission_90 = Permission()
    auth_permission_90.name = u'Can add form log plugin'
    auth_permission_90.content_type = ContentType.objects.get(app_label="myforms", model="formlogplugin")
    auth_permission_90.codename = u'add_formlogplugin'
    auth_permission_90.save()

    auth_permission_91 = Permission()
    auth_permission_91.name = u'Can change form log plugin'
    auth_permission_91.content_type = ContentType.objects.get(app_label="myforms", model="formlogplugin")
    auth_permission_91.codename = u'change_formlogplugin'
    auth_permission_91.save()

    auth_permission_92 = Permission()
    auth_permission_92.name = u'Can delete form log plugin'
    auth_permission_92.content_type = ContentType.objects.get(app_label="myforms", model="formlogplugin")
    auth_permission_92.codename = u'delete_formlogplugin'
    auth_permission_92.save()

    auth_permission_93 = Permission()
    auth_permission_93.name = u'Can add options'
    auth_permission_93.content_type = ContentType.objects.get(app_label="options", model="options")
    auth_permission_93.codename = u'add_options'
    auth_permission_93.save()

    auth_permission_94 = Permission()
    auth_permission_94.name = u'Can change options'
    auth_permission_94.content_type = ContentType.objects.get(app_label="options", model="options")
    auth_permission_94.codename = u'change_options'
    auth_permission_94.save()

    auth_permission_95 = Permission()
    auth_permission_95.name = u'Can delete options'
    auth_permission_95.content_type = ContentType.objects.get(app_label="options", model="options")
    auth_permission_95.codename = u'delete_options'
    auth_permission_95.save()

    auth_permission_96 = Permission()
    auth_permission_96.name = u'Can add session'
    auth_permission_96.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_96.codename = u'add_session'
    auth_permission_96.save()

    auth_permission_97 = Permission()
    auth_permission_97.name = u'Can change session'
    auth_permission_97.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_97.codename = u'change_session'
    auth_permission_97.save()

    auth_permission_98 = Permission()
    auth_permission_98.name = u'Can delete session'
    auth_permission_98.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_98.codename = u'delete_session'
    auth_permission_98.save()

    auth_permission_99 = Permission()
    auth_permission_99.name = u'Can add site'
    auth_permission_99.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_99.codename = u'add_site'
    auth_permission_99.save()

    auth_permission_100 = Permission()
    auth_permission_100.name = u'Can change site'
    auth_permission_100.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_100.codename = u'change_site'
    auth_permission_100.save()

    auth_permission_101 = Permission()
    auth_permission_101.name = u'Can delete site'
    auth_permission_101.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_101.codename = u'delete_site'
    auth_permission_101.save()

    auth_permission_102 = Permission()
    auth_permission_102.name = u'Can add migration history'
    auth_permission_102.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_102.codename = u'add_migrationhistory'
    auth_permission_102.save()

    auth_permission_103 = Permission()
    auth_permission_103.name = u'Can change migration history'
    auth_permission_103.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_103.codename = u'change_migrationhistory'
    auth_permission_103.save()

    auth_permission_104 = Permission()
    auth_permission_104.name = u'Can delete migration history'
    auth_permission_104.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_104.codename = u'delete_migrationhistory'
    auth_permission_104.save()

    auth_permission_105 = Permission()
    auth_permission_105.name = u'Can add text'
    auth_permission_105.content_type = ContentType.objects.get(app_label="text", model="text")
    auth_permission_105.codename = u'add_text'
    auth_permission_105.save()

    auth_permission_106 = Permission()
    auth_permission_106.name = u'Can change text'
    auth_permission_106.content_type = ContentType.objects.get(app_label="text", model="text")
    auth_permission_106.codename = u'change_text'
    auth_permission_106.save()

    auth_permission_107 = Permission()
    auth_permission_107.name = u'Can delete text'
    auth_permission_107.content_type = ContentType.objects.get(app_label="text", model="text")
    auth_permission_107.codename = u'delete_text'
    auth_permission_107.save()

    from django.contrib.auth.models import Group


    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.username = u'admin'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u'a@a.ru'
    auth_user_1.password = u'pbkdf2_sha256$10000$zcns7unj2mO3$CxjEuzz7EiEzCBcgVCaaC+/1Eor8Q/mqKY9oRGjji7U='
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.is_superuser = True
    auth_user_1.last_login = datetime.datetime(2012, 8, 31, 11, 33, 6, 891369, tzinfo=utc)
    auth_user_1.date_joined = datetime.datetime(2012, 8, 29, 11, 29, 31, 662519, tzinfo=utc)
    auth_user_1.save()

    from django.contrib.sessions.models import Session

    django_session_1 = Session()
    django_session_1.session_key = u'042719829b6545f4848097bf9efe326b'
    django_session_1.session_data = u'OWFkOGIyMzY2OTk3NjI1ZDU4Yzk1NjI4ZWFiOWNhODMxZjNmMzNmMDqAAn1xAS4=\n'
    django_session_1.expire_date = datetime.datetime(2012, 9, 13, 12, 19, 20, 556432, tzinfo=utc)
    django_session_1.save()

    django_session_2 = Session()
    django_session_2.session_key = u'8f20496da3b3c34c03a7f394c72312c3'
    django_session_2.session_data = u'OTViZjU3MTRkNGJhYjM4ZDg0ZjVmNzJlMTcwY2FjMjdmNTcyNDlmMzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRVD2Rq\nYW5nb19sYW5ndWFnZVgCAAAAcnVxAlUNX2F1dGhfdXNlcl9pZEsBdS4=\n'
    django_session_2.expire_date = datetime.datetime(2012, 9, 14, 11, 34, 2, 547826, tzinfo=utc)
    django_session_2.save()

    from django.contrib.sites.models import Site

    django_site_1 = Site()
    django_site_1.domain = u'example.com'
    django_site_1.name = u'example.com'
    django_site_1.save()

    from django.contrib.admin.models import LogEntry

    django_admin_log_1 = LogEntry()
    django_admin_log_1.action_time = datetime.datetime(2012, 8, 30, 11, 21, 20, 707273, tzinfo=utc)
    django_admin_log_1.user = auth_user_1
    django_admin_log_1.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_1.object_id = u'5'
    django_admin_log_1.object_repr = u'\u041e\u043f\u0442\u043e\u0432\u044b\u0435 \u0437\u0430\u043a\u0443\u043f\u043a\u0438'
    django_admin_log_1.action_flag = 2
    django_admin_log_1.change_message = u'\u0418\u0437\u043c\u0435\u043d\u0435\u043d moderator_state.'
    django_admin_log_1.save()

    django_admin_log_2 = LogEntry()
    django_admin_log_2.action_time = datetime.datetime(2012, 8, 30, 11, 19, 44, 503558, tzinfo=utc)
    django_admin_log_2.user = auth_user_1
    django_admin_log_2.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_2.object_id = u'4'
    django_admin_log_2.object_repr = u'\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b'
    django_admin_log_2.action_flag = 2
    django_admin_log_2.change_message = u'\u0418\u0437\u043c\u0435\u043d\u0435\u043d moderator_state.'
    django_admin_log_2.save()

    django_admin_log_3 = LogEntry()
    django_admin_log_3.action_time = datetime.datetime(2012, 8, 30, 11, 16, 20, 324888, tzinfo=utc)
    django_admin_log_3.user = auth_user_1
    django_admin_log_3.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_3.object_id = u'3'
    django_admin_log_3.object_repr = u'\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430'
    django_admin_log_3.action_flag = 2
    django_admin_log_3.change_message = u'\u0418\u0437\u043c\u0435\u043d\u0435\u043d moderator_state.'
    django_admin_log_3.save()

    django_admin_log_4 = LogEntry()
    django_admin_log_4.action_time = datetime.datetime(2012, 8, 30, 11, 14, 30, 230650, tzinfo=utc)
    django_admin_log_4.user = auth_user_1
    django_admin_log_4.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_4.object_id = u'1'
    django_admin_log_4.object_repr = u'\u0413\u043b\u0430\u0432\u043d\u0430\u044f'
    django_admin_log_4.action_flag = 2
    django_admin_log_4.change_message = u'\u0418\u0437\u043c\u0435\u043d\u0435\u043d moderator_state.'
    django_admin_log_4.save()

    django_admin_log_5 = LogEntry()
    django_admin_log_5.action_time = datetime.datetime(2012, 8, 30, 11, 11, 42, 391886, tzinfo=utc)
    django_admin_log_5.user = auth_user_1
    django_admin_log_5.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_5.object_id = u'1'
    django_admin_log_5.object_repr = u'\u0413\u043b\u0430\u0432\u043d\u0430\u044f'
    django_admin_log_5.action_flag = 2
    django_admin_log_5.change_message = u'\u0418\u0437\u043c\u0435\u043d\u0435\u043d moderator_state.'
    django_admin_log_5.save()

    django_admin_log_6 = LogEntry()
    django_admin_log_6.action_time = datetime.datetime(2012, 8, 30, 11, 0, 55, 540868, tzinfo=utc)
    django_admin_log_6.user = auth_user_1
    django_admin_log_6.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_6.object_id = u'5'
    django_admin_log_6.object_repr = u'\u041e\u043f\u0442\u043e\u0432\u044b\u0435 \u0437\u0430\u043a\u0443\u043f\u043a\u0438'
    django_admin_log_6.action_flag = 1
    django_admin_log_6.change_message = u''
    django_admin_log_6.save()

    django_admin_log_7 = LogEntry()
    django_admin_log_7.action_time = datetime.datetime(2012, 8, 30, 11, 0, 29, 201590, tzinfo=utc)
    django_admin_log_7.user = auth_user_1
    django_admin_log_7.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_7.object_id = u'4'
    django_admin_log_7.object_repr = u'\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b'
    django_admin_log_7.action_flag = 1
    django_admin_log_7.change_message = u''
    django_admin_log_7.save()

    django_admin_log_8 = LogEntry()
    django_admin_log_8.action_time = datetime.datetime(2012, 8, 30, 10, 58, 29, 716663, tzinfo=utc)
    django_admin_log_8.user = auth_user_1
    django_admin_log_8.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_8.object_id = u'3'
    django_admin_log_8.object_repr = u'\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430'
    django_admin_log_8.action_flag = 1
    django_admin_log_8.change_message = u''
    django_admin_log_8.save()

    django_admin_log_9 = LogEntry()
    django_admin_log_9.action_time = datetime.datetime(2012, 8, 29, 11, 31, 46, 232627, tzinfo=utc)
    django_admin_log_9.user = auth_user_1
    django_admin_log_9.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_9.object_id = u'1'
    django_admin_log_9.object_repr = u'\u0413\u043b\u0430\u0432\u043d\u0430\u044f'
    django_admin_log_9.action_flag = 2
    django_admin_log_9.change_message = u'\u0418\u0437\u043c\u0435\u043d\u0435\u043d moderator_state.'
    django_admin_log_9.save()

    django_admin_log_10 = LogEntry()
    django_admin_log_10.action_time = datetime.datetime(2012, 8, 29, 11, 31, 38, 139209, tzinfo=utc)
    django_admin_log_10.user = auth_user_1
    django_admin_log_10.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_10.object_id = u'2'
    django_admin_log_10.object_repr = u'\u0417\u0430\u043a\u0430\u0437\u0430\u0442\u044c'
    django_admin_log_10.action_flag = 2
    django_admin_log_10.change_message = u'\u0418\u0437\u043c\u0435\u043d\u0435\u043d moderator_state.'
    django_admin_log_10.save()

    django_admin_log_11 = LogEntry()
    django_admin_log_11.action_time = datetime.datetime(2012, 8, 29, 11, 30, 37, 436958, tzinfo=utc)
    django_admin_log_11.user = auth_user_1
    django_admin_log_11.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_11.object_id = u'2'
    django_admin_log_11.object_repr = u'\u0417\u0430\u043a\u0430\u0437\u0430\u0442\u044c'
    django_admin_log_11.action_flag = 2
    django_admin_log_11.change_message = u'\u0418\u0437\u043c\u0435\u043d\u0435\u043d moderator_state.'
    django_admin_log_11.save()

    django_admin_log_12 = LogEntry()
    django_admin_log_12.action_time = datetime.datetime(2012, 8, 29, 11, 30, 26, 453380, tzinfo=utc)
    django_admin_log_12.user = auth_user_1
    django_admin_log_12.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_12.object_id = u'2'
    django_admin_log_12.object_repr = u'\u0417\u0430\u043a\u0430\u0437\u0430\u0442\u044c'
    django_admin_log_12.action_flag = 2
    django_admin_log_12.change_message = u'\u0418\u0437\u043c\u0435\u043d\u0435\u043d published,in_navigation \u0438 moderator_state.'
    django_admin_log_12.save()

    django_admin_log_13 = LogEntry()
    django_admin_log_13.action_time = datetime.datetime(2012, 8, 29, 11, 30, 16, 719928, tzinfo=utc)
    django_admin_log_13.user = auth_user_1
    django_admin_log_13.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_13.object_id = u'2'
    django_admin_log_13.object_repr = u'\u0417\u0430\u043a\u0430\u0437\u0430\u0442\u044c'
    django_admin_log_13.action_flag = 1
    django_admin_log_13.change_message = u''
    django_admin_log_13.save()

    django_admin_log_14 = LogEntry()
    django_admin_log_14.action_time = datetime.datetime(2012, 8, 29, 11, 30, 7, 397112, tzinfo=utc)
    django_admin_log_14.user = auth_user_1
    django_admin_log_14.content_type = ContentType.objects.get(app_label="cms", model="page")
    django_admin_log_14.object_id = u'1'
    django_admin_log_14.object_repr = u'\u0413\u043b\u0430\u0432\u043d\u0430\u044f'
    django_admin_log_14.action_flag = 1
    django_admin_log_14.change_message = u''
    django_admin_log_14.save()

    from cms.models.placeholdermodel import Placeholder

    cms_placeholder_1 = Placeholder()
    cms_placeholder_1.slot = u'slider'
    cms_placeholder_1.default_width = None
    cms_placeholder_1.save()

    cms_placeholder_2 = Placeholder()
    cms_placeholder_2.slot = u'content'
    cms_placeholder_2.default_width = None
    cms_placeholder_2.save()

    cms_placeholder_3 = Placeholder()
    cms_placeholder_3.slot = u'slider'
    cms_placeholder_3.default_width = None
    cms_placeholder_3.save()

    cms_placeholder_4 = Placeholder()
    cms_placeholder_4.slot = u'content'
    cms_placeholder_4.default_width = None
    cms_placeholder_4.save()

    cms_placeholder_5 = Placeholder()
    cms_placeholder_5.slot = u'slider'
    cms_placeholder_5.default_width = None
    cms_placeholder_5.save()

    cms_placeholder_6 = Placeholder()
    cms_placeholder_6.slot = u'content'
    cms_placeholder_6.default_width = None
    cms_placeholder_6.save()

    cms_placeholder_7 = Placeholder()
    cms_placeholder_7.slot = u'slider'
    cms_placeholder_7.default_width = None
    cms_placeholder_7.save()

    cms_placeholder_8 = Placeholder()
    cms_placeholder_8.slot = u'content'
    cms_placeholder_8.default_width = None
    cms_placeholder_8.save()

    cms_placeholder_9 = Placeholder()
    cms_placeholder_9.slot = u'slider'
    cms_placeholder_9.default_width = None
    cms_placeholder_9.save()

    cms_placeholder_10 = Placeholder()
    cms_placeholder_10.slot = u'content'
    cms_placeholder_10.default_width = None
    cms_placeholder_10.save()

    from cms.models.pluginmodel import CMSPlugin


    from cms.models.pagemodel import Page

    cms_page_1 = Page()
    cms_page_1.created_by = u'admin'
    cms_page_1.changed_by = u'admin'
    cms_page_1.parent = None
    cms_page_1.creation_date = datetime.datetime(2012, 8, 29, 11, 30, 7, 182137, tzinfo=utc)
    cms_page_1.changed_date = datetime.datetime(2012, 8, 30, 11, 14, 29, 302659, tzinfo=utc)
    cms_page_1.publication_date = datetime.datetime(2012, 8, 29, 11, 30, 41, 154576, tzinfo=utc)
    cms_page_1.publication_end_date = None
    cms_page_1.in_navigation = True
    cms_page_1.soft_root = False
    cms_page_1.reverse_id = None
    cms_page_1.navigation_extenders = u''
    cms_page_1.published = True
    cms_page_1.template = u'index.html'
    cms_page_1.site = django_site_1
    cms_page_1.moderator_state = 0
    cms_page_1.level = 0
    cms_page_1.lft = 1
    cms_page_1.rght = 2
    cms_page_1.tree_id = 1
    cms_page_1.login_required = False
    cms_page_1.limit_visibility_in_menu = None
    cms_page_1.publisher_is_draft = True
    cms_page_1.publisher_public = None
    cms_page_1.publisher_state = 1
    cms_page_1.save()

    cms_page_1.placeholders.add(cms_placeholder_1)
    cms_page_1.placeholders.add(cms_placeholder_2)

    cms_page_2 = Page()
    cms_page_2.created_by = u'admin'
    cms_page_2.changed_by = u'admin'
    cms_page_2.parent = None
    cms_page_2.creation_date = datetime.datetime(2012, 8, 29, 11, 30, 16, 524836, tzinfo=utc)
    cms_page_2.changed_date = datetime.datetime(2012, 8, 29, 11, 31, 37, 983018, tzinfo=utc)
    cms_page_2.publication_date = datetime.datetime(2012, 8, 29, 11, 30, 26, 259024, tzinfo=utc)
    cms_page_2.publication_end_date = None
    cms_page_2.in_navigation = True
    cms_page_2.soft_root = False
    cms_page_2.reverse_id = None
    cms_page_2.navigation_extenders = u''
    cms_page_2.published = True
    cms_page_2.template = u'index.html'
    cms_page_2.site = django_site_1
    cms_page_2.moderator_state = 0
    cms_page_2.level = 0
    cms_page_2.lft = 1
    cms_page_2.rght = 2
    cms_page_2.tree_id = 2
    cms_page_2.login_required = False
    cms_page_2.limit_visibility_in_menu = None
    cms_page_2.publisher_is_draft = True
    cms_page_2.publisher_public = None
    cms_page_2.publisher_state = 1
    cms_page_2.save()

    cms_page_2.placeholders.add(cms_placeholder_3)
    cms_page_2.placeholders.add(cms_placeholder_4)

    cms_page_3 = Page()
    cms_page_3.created_by = u'admin'
    cms_page_3.changed_by = u'admin'
    cms_page_3.parent = None
    cms_page_3.creation_date = datetime.datetime(2012, 8, 30, 10, 58, 28, 491342, tzinfo=utc)
    cms_page_3.changed_date = datetime.datetime(2012, 8, 30, 11, 16, 19, 355647, tzinfo=utc)
    cms_page_3.publication_date = datetime.datetime(2012, 8, 30, 11, 1, 2, 718140, tzinfo=utc)
    cms_page_3.publication_end_date = None
    cms_page_3.in_navigation = True
    cms_page_3.soft_root = False
    cms_page_3.reverse_id = None
    cms_page_3.navigation_extenders = u''
    cms_page_3.published = True
    cms_page_3.template = u'index.html'
    cms_page_3.site = django_site_1
    cms_page_3.moderator_state = 0
    cms_page_3.level = 0
    cms_page_3.lft = 1
    cms_page_3.rght = 2
    cms_page_3.tree_id = 3
    cms_page_3.login_required = False
    cms_page_3.limit_visibility_in_menu = None
    cms_page_3.publisher_is_draft = True
    cms_page_3.publisher_public = None
    cms_page_3.publisher_state = 1
    cms_page_3.save()

    cms_page_3.placeholders.add(cms_placeholder_5)
    cms_page_3.placeholders.add(cms_placeholder_6)

    cms_page_4 = Page()
    cms_page_4.created_by = u'admin'
    cms_page_4.changed_by = u'admin'
    cms_page_4.parent = None
    cms_page_4.creation_date = datetime.datetime(2012, 8, 30, 11, 0, 27, 984165, tzinfo=utc)
    cms_page_4.changed_date = datetime.datetime(2012, 8, 30, 11, 19, 43, 572539, tzinfo=utc)
    cms_page_4.publication_date = datetime.datetime(2012, 8, 30, 11, 1, 6, 310345, tzinfo=utc)
    cms_page_4.publication_end_date = None
    cms_page_4.in_navigation = True
    cms_page_4.soft_root = False
    cms_page_4.reverse_id = None
    cms_page_4.navigation_extenders = u''
    cms_page_4.published = True
    cms_page_4.template = u'index.html'
    cms_page_4.site = django_site_1
    cms_page_4.moderator_state = 0
    cms_page_4.level = 0
    cms_page_4.lft = 1
    cms_page_4.rght = 2
    cms_page_4.tree_id = 4
    cms_page_4.login_required = False
    cms_page_4.limit_visibility_in_menu = None
    cms_page_4.publisher_is_draft = True
    cms_page_4.publisher_public = None
    cms_page_4.publisher_state = 1
    cms_page_4.save()

    cms_page_4.placeholders.add(cms_placeholder_7)
    cms_page_4.placeholders.add(cms_placeholder_8)

    cms_page_5 = Page()
    cms_page_5.created_by = u'admin'
    cms_page_5.changed_by = u'admin'
    cms_page_5.parent = None
    cms_page_5.creation_date = datetime.datetime(2012, 8, 30, 11, 0, 54, 219622, tzinfo=utc)
    cms_page_5.changed_date = datetime.datetime(2012, 8, 30, 11, 21, 19, 728062, tzinfo=utc)
    cms_page_5.publication_date = datetime.datetime(2012, 8, 30, 11, 1, 10, 196307, tzinfo=utc)
    cms_page_5.publication_end_date = None
    cms_page_5.in_navigation = True
    cms_page_5.soft_root = False
    cms_page_5.reverse_id = None
    cms_page_5.navigation_extenders = u''
    cms_page_5.published = True
    cms_page_5.template = u'index.html'
    cms_page_5.site = django_site_1
    cms_page_5.moderator_state = 0
    cms_page_5.level = 0
    cms_page_5.lft = 1
    cms_page_5.rght = 2
    cms_page_5.tree_id = 5
    cms_page_5.login_required = False
    cms_page_5.limit_visibility_in_menu = None
    cms_page_5.publisher_is_draft = True
    cms_page_5.publisher_public = None
    cms_page_5.publisher_state = 1
    cms_page_5.save()

    cms_page_5.placeholders.add(cms_placeholder_9)
    cms_page_5.placeholders.add(cms_placeholder_10)

    from cms.models.moderatormodels import PageModerator


    from cms.models.moderatormodels import PageModeratorState


    from cms.models.permissionmodels import GlobalPagePermission


    from cms.models.permissionmodels import PagePermission


    from cms.models.permissionmodels import PageUser


    from cms.models.permissionmodels import PageUserGroup


    from cms.models.titlemodels import Title

    cms_title_1 = Title()
    cms_title_1.language = u'ru'
    cms_title_1.title = u'\u0417\u0430\u043a\u0430\u0437\u0430\u0442\u044c'
    cms_title_1.menu_title = u''
    cms_title_1.slug = u'zakazat'
    cms_title_1.path = u'zakazat'
    cms_title_1.has_url_overwrite = False
    cms_title_1.application_urls = u''
    cms_title_1.redirect = u''
    cms_title_1.meta_description = u''
    cms_title_1.meta_keywords = u''
    cms_title_1.page_title = u''
    cms_title_1.page = cms_page_2
    cms_title_1.creation_date = datetime.datetime(2012, 8, 29, 11, 30, 16, 617709, tzinfo=utc)
    cms_title_1.save()

    cms_title_2 = Title()
    cms_title_2.language = u'ru'
    cms_title_2.title = u'\u0413\u043b\u0430\u0432\u043d\u0430\u044f'
    cms_title_2.menu_title = u''
    cms_title_2.slug = u'main'
    cms_title_2.path = u''
    cms_title_2.has_url_overwrite = False
    cms_title_2.application_urls = u''
    cms_title_2.redirect = u''
    cms_title_2.meta_description = u''
    cms_title_2.meta_keywords = u''
    cms_title_2.page_title = u''
    cms_title_2.page = cms_page_1
    cms_title_2.creation_date = datetime.datetime(2012, 8, 29, 11, 30, 7, 277258, tzinfo=utc)
    cms_title_2.save()

    cms_title_3 = Title()
    cms_title_3.language = u'ru'
    cms_title_3.title = u'\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430'
    cms_title_3.menu_title = u''
    cms_title_3.slug = u'dostavka'
    cms_title_3.path = u'dostavka'
    cms_title_3.has_url_overwrite = False
    cms_title_3.application_urls = u''
    cms_title_3.redirect = u''
    cms_title_3.meta_description = u''
    cms_title_3.meta_keywords = u''
    cms_title_3.page_title = u''
    cms_title_3.page = cms_page_3
    cms_title_3.creation_date = datetime.datetime(2012, 8, 30, 10, 58, 29, 146557, tzinfo=utc)
    cms_title_3.save()

    cms_title_4 = Title()
    cms_title_4.language = u'ru'
    cms_title_4.title = u'\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b'
    cms_title_4.menu_title = u''
    cms_title_4.slug = u'kontakty'
    cms_title_4.path = u'kontakty'
    cms_title_4.has_url_overwrite = False
    cms_title_4.application_urls = u''
    cms_title_4.redirect = u''
    cms_title_4.meta_description = u''
    cms_title_4.meta_keywords = u''
    cms_title_4.page_title = u''
    cms_title_4.page = cms_page_4
    cms_title_4.creation_date = datetime.datetime(2012, 8, 30, 11, 0, 28, 682108, tzinfo=utc)
    cms_title_4.save()

    cms_title_5 = Title()
    cms_title_5.language = u'ru'
    cms_title_5.title = u'\u041e\u043f\u0442\u043e\u0432\u044b\u0435 \u0437\u0430\u043a\u0443\u043f\u043a\u0438'
    cms_title_5.menu_title = u''
    cms_title_5.slug = u'optovye-zakupki'
    cms_title_5.path = u'optovye-zakupki'
    cms_title_5.has_url_overwrite = False
    cms_title_5.application_urls = u''
    cms_title_5.redirect = u''
    cms_title_5.meta_description = u''
    cms_title_5.meta_keywords = u''
    cms_title_5.page_title = u''
    cms_title_5.page = cms_page_5
    cms_title_5.creation_date = datetime.datetime(2012, 8, 30, 11, 0, 54, 889924, tzinfo=utc)
    cms_title_5.save()

    from south.models import MigrationHistory

    south_migrationhistory_1 = MigrationHistory()
    south_migrationhistory_1.app_name = u'cms'
    south_migrationhistory_1.migration = u'0001_initial'
    south_migrationhistory_1.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 834731, tzinfo=utc)
    south_migrationhistory_1.save()

    south_migrationhistory_2 = MigrationHistory()
    south_migrationhistory_2.app_name = u'cms'
    south_migrationhistory_2.migration = u'0002_auto_start'
    south_migrationhistory_2.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 846339, tzinfo=utc)
    south_migrationhistory_2.save()

    south_migrationhistory_3 = MigrationHistory()
    south_migrationhistory_3.app_name = u'cms'
    south_migrationhistory_3.migration = u'0003_remove_placeholder'
    south_migrationhistory_3.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 854926, tzinfo=utc)
    south_migrationhistory_3.save()

    south_migrationhistory_4 = MigrationHistory()
    south_migrationhistory_4.app_name = u'cms'
    south_migrationhistory_4.migration = u'0004_textobjects'
    south_migrationhistory_4.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 863003, tzinfo=utc)
    south_migrationhistory_4.save()

    south_migrationhistory_5 = MigrationHistory()
    south_migrationhistory_5.app_name = u'cms'
    south_migrationhistory_5.migration = u'0005_mptt_added_to_plugins'
    south_migrationhistory_5.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 872129, tzinfo=utc)
    south_migrationhistory_5.save()

    south_migrationhistory_6 = MigrationHistory()
    south_migrationhistory_6.app_name = u'text'
    south_migrationhistory_6.migration = u'0001_initial'
    south_migrationhistory_6.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 885786, tzinfo=utc)
    south_migrationhistory_6.save()

    south_migrationhistory_7 = MigrationHistory()
    south_migrationhistory_7.app_name = u'text'
    south_migrationhistory_7.migration = u'0002_freeze'
    south_migrationhistory_7.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 892630, tzinfo=utc)
    south_migrationhistory_7.save()

    south_migrationhistory_8 = MigrationHistory()
    south_migrationhistory_8.app_name = u'cms'
    south_migrationhistory_8.migration = u'0006_apphook'
    south_migrationhistory_8.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 899392, tzinfo=utc)
    south_migrationhistory_8.save()

    south_migrationhistory_9 = MigrationHistory()
    south_migrationhistory_9.app_name = u'cms'
    south_migrationhistory_9.migration = u'0007_apphook_longer'
    south_migrationhistory_9.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 907487, tzinfo=utc)
    south_migrationhistory_9.save()

    south_migrationhistory_10 = MigrationHistory()
    south_migrationhistory_10.app_name = u'cms'
    south_migrationhistory_10.migration = u'0008_redirects'
    south_migrationhistory_10.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 914490, tzinfo=utc)
    south_migrationhistory_10.save()

    south_migrationhistory_11 = MigrationHistory()
    south_migrationhistory_11.app_name = u'cms'
    south_migrationhistory_11.migration = u'0009_added_meta_fields'
    south_migrationhistory_11.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 921791, tzinfo=utc)
    south_migrationhistory_11.save()

    south_migrationhistory_12 = MigrationHistory()
    south_migrationhistory_12.app_name = u'cms'
    south_migrationhistory_12.migration = u'0010_5char_language'
    south_migrationhistory_12.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 929017, tzinfo=utc)
    south_migrationhistory_12.save()

    south_migrationhistory_13 = MigrationHistory()
    south_migrationhistory_13.app_name = u'cms'
    south_migrationhistory_13.migration = u'0011_title_overwrites'
    south_migrationhistory_13.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 936267, tzinfo=utc)
    south_migrationhistory_13.save()

    south_migrationhistory_14 = MigrationHistory()
    south_migrationhistory_14.app_name = u'cms'
    south_migrationhistory_14.migration = u'0012_publisher'
    south_migrationhistory_14.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 945269, tzinfo=utc)
    south_migrationhistory_14.save()

    south_migrationhistory_15 = MigrationHistory()
    south_migrationhistory_15.app_name = u'text'
    south_migrationhistory_15.migration = u'0003_publisher'
    south_migrationhistory_15.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 953052, tzinfo=utc)
    south_migrationhistory_15.save()

    south_migrationhistory_16 = MigrationHistory()
    south_migrationhistory_16.app_name = u'cms'
    south_migrationhistory_16.migration = u'0013_site_copy'
    south_migrationhistory_16.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 960967, tzinfo=utc)
    south_migrationhistory_16.save()

    south_migrationhistory_17 = MigrationHistory()
    south_migrationhistory_17.app_name = u'cms'
    south_migrationhistory_17.migration = u'0014_sites_removed'
    south_migrationhistory_17.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 970954, tzinfo=utc)
    south_migrationhistory_17.save()

    south_migrationhistory_18 = MigrationHistory()
    south_migrationhistory_18.app_name = u'cms'
    south_migrationhistory_18.migration = u'0015_modified_by_added'
    south_migrationhistory_18.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 977996, tzinfo=utc)
    south_migrationhistory_18.save()

    south_migrationhistory_19 = MigrationHistory()
    south_migrationhistory_19.app_name = u'cms'
    south_migrationhistory_19.migration = u'0016_author_copy'
    south_migrationhistory_19.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 985273, tzinfo=utc)
    south_migrationhistory_19.save()

    south_migrationhistory_20 = MigrationHistory()
    south_migrationhistory_20.app_name = u'cms'
    south_migrationhistory_20.migration = u'0017_author_removed'
    south_migrationhistory_20.applied = datetime.datetime(2012, 8, 29, 11, 29, 39, 992270, tzinfo=utc)
    south_migrationhistory_20.save()

    south_migrationhistory_21 = MigrationHistory()
    south_migrationhistory_21.app_name = u'cms'
    south_migrationhistory_21.migration = u'0018_site_permissions'
    south_migrationhistory_21.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 2754, tzinfo=utc)
    south_migrationhistory_21.save()

    south_migrationhistory_22 = MigrationHistory()
    south_migrationhistory_22.app_name = u'cms'
    south_migrationhistory_22.migration = u'0019_public_table_renames'
    south_migrationhistory_22.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 12089, tzinfo=utc)
    south_migrationhistory_22.save()

    south_migrationhistory_23 = MigrationHistory()
    south_migrationhistory_23.app_name = u'text'
    south_migrationhistory_23.migration = u'0004_table_rename'
    south_migrationhistory_23.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 19960, tzinfo=utc)
    south_migrationhistory_23.save()

    south_migrationhistory_24 = MigrationHistory()
    south_migrationhistory_24.app_name = u'text'
    south_migrationhistory_24.migration = u'0005_publisher2'
    south_migrationhistory_24.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 29453, tzinfo=utc)
    south_migrationhistory_24.save()

    south_migrationhistory_25 = MigrationHistory()
    south_migrationhistory_25.app_name = u'cms'
    south_migrationhistory_25.migration = u'0020_advanced_permissions'
    south_migrationhistory_25.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 36140, tzinfo=utc)
    south_migrationhistory_25.save()

    south_migrationhistory_26 = MigrationHistory()
    south_migrationhistory_26.app_name = u'cms'
    south_migrationhistory_26.migration = u'0021_publisher2'
    south_migrationhistory_26.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 43031, tzinfo=utc)
    south_migrationhistory_26.save()

    south_migrationhistory_27 = MigrationHistory()
    south_migrationhistory_27.app_name = u'cms'
    south_migrationhistory_27.migration = u'0022_login_required_added'
    south_migrationhistory_27.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 50703, tzinfo=utc)
    south_migrationhistory_27.save()

    south_migrationhistory_28 = MigrationHistory()
    south_migrationhistory_28.app_name = u'cms'
    south_migrationhistory_28.migration = u'0023_plugin_table_naming_function_changed'
    south_migrationhistory_28.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 60675, tzinfo=utc)
    south_migrationhistory_28.save()

    south_migrationhistory_29 = MigrationHistory()
    south_migrationhistory_29.app_name = u'cms'
    south_migrationhistory_29.migration = u'0024_added_placeholder_model'
    south_migrationhistory_29.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 68710, tzinfo=utc)
    south_migrationhistory_29.save()

    south_migrationhistory_30 = MigrationHistory()
    south_migrationhistory_30.app_name = u'cms'
    south_migrationhistory_30.migration = u'0025_placeholder_migration'
    south_migrationhistory_30.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 76234, tzinfo=utc)
    south_migrationhistory_30.save()

    south_migrationhistory_31 = MigrationHistory()
    south_migrationhistory_31.app_name = u'cms'
    south_migrationhistory_31.migration = u'0026_finish_placeholder_migration'
    south_migrationhistory_31.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 84257, tzinfo=utc)
    south_migrationhistory_31.save()

    south_migrationhistory_32 = MigrationHistory()
    south_migrationhistory_32.app_name = u'cms'
    south_migrationhistory_32.migration = u'0027_added_width_to_placeholder'
    south_migrationhistory_32.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 92550, tzinfo=utc)
    south_migrationhistory_32.save()

    south_migrationhistory_33 = MigrationHistory()
    south_migrationhistory_33.app_name = u'cms'
    south_migrationhistory_33.migration = u'0028_limit_visibility_in_menu_step1of3'
    south_migrationhistory_33.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 102458, tzinfo=utc)
    south_migrationhistory_33.save()

    south_migrationhistory_34 = MigrationHistory()
    south_migrationhistory_34.app_name = u'cms'
    south_migrationhistory_34.migration = u'0029_limit_visibility_in_menu_step2of3_data'
    south_migrationhistory_34.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 110678, tzinfo=utc)
    south_migrationhistory_34.save()

    south_migrationhistory_35 = MigrationHistory()
    south_migrationhistory_35.app_name = u'cms'
    south_migrationhistory_35.migration = u'0030_limit_visibility_in_menu_step3of3'
    south_migrationhistory_35.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 119316, tzinfo=utc)
    south_migrationhistory_35.save()

    south_migrationhistory_36 = MigrationHistory()
    south_migrationhistory_36.app_name = u'cms'
    south_migrationhistory_36.migration = u'0031_improved_language_code_support'
    south_migrationhistory_36.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 128478, tzinfo=utc)
    south_migrationhistory_36.save()

    south_migrationhistory_37 = MigrationHistory()
    south_migrationhistory_37.app_name = u'cms'
    south_migrationhistory_37.migration = u'0032_auto__del_field_cmsplugin_publisher_public__del_field_cmsplugin_publis'
    south_migrationhistory_37.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 135614, tzinfo=utc)
    south_migrationhistory_37.save()

    south_migrationhistory_38 = MigrationHistory()
    south_migrationhistory_38.app_name = u'cms'
    south_migrationhistory_38.migration = u'0033_auto__del_field_title_publisher_is_draft__del_field_title_publisher_st'
    south_migrationhistory_38.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 142650, tzinfo=utc)
    south_migrationhistory_38.save()

    south_migrationhistory_39 = MigrationHistory()
    south_migrationhistory_39.app_name = u'cms'
    south_migrationhistory_39.migration = u'0034_auto__chg_field_title_language__chg_field_cmsplugin_language__add_fiel'
    south_migrationhistory_39.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 149887, tzinfo=utc)
    south_migrationhistory_39.save()

    south_migrationhistory_40 = MigrationHistory()
    south_migrationhistory_40.app_name = u'cms'
    south_migrationhistory_40.migration = u'0035_auto__add_field_globalpagepermission_can_view__add_field_pagepermissio'
    south_migrationhistory_40.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 159522, tzinfo=utc)
    south_migrationhistory_40.save()

    south_migrationhistory_41 = MigrationHistory()
    south_migrationhistory_41.app_name = u'menus'
    south_migrationhistory_41.migration = u'0001_initial'
    south_migrationhistory_41.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 202096, tzinfo=utc)
    south_migrationhistory_41.save()

    south_migrationhistory_42 = MigrationHistory()
    south_migrationhistory_42.app_name = u'text'
    south_migrationhistory_42.migration = u'0006_2_1_4_upgrade'
    south_migrationhistory_42.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 254141, tzinfo=utc)
    south_migrationhistory_42.save()

    south_migrationhistory_43 = MigrationHistory()
    south_migrationhistory_43.app_name = u'text'
    south_migrationhistory_43.migration = u'0007_initial'
    south_migrationhistory_43.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 261529, tzinfo=utc)
    south_migrationhistory_43.save()

    south_migrationhistory_44 = MigrationHistory()
    south_migrationhistory_44.app_name = u'filer'
    south_migrationhistory_44.migration = u'0001_initial'
    south_migrationhistory_44.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 303064, tzinfo=utc)
    south_migrationhistory_44.save()

    south_migrationhistory_45 = MigrationHistory()
    south_migrationhistory_45.app_name = u'filer'
    south_migrationhistory_45.migration = u'0002_rename_file_field'
    south_migrationhistory_45.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 310275, tzinfo=utc)
    south_migrationhistory_45.save()

    south_migrationhistory_46 = MigrationHistory()
    south_migrationhistory_46.app_name = u'filer'
    south_migrationhistory_46.migration = u'0003_add_description_field'
    south_migrationhistory_46.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 319180, tzinfo=utc)
    south_migrationhistory_46.save()

    south_migrationhistory_47 = MigrationHistory()
    south_migrationhistory_47.app_name = u'filer'
    south_migrationhistory_47.migration = u'0004_auto__del_field_file__file__add_field_file_file__add_field_file_is_pub'
    south_migrationhistory_47.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 326350, tzinfo=utc)
    south_migrationhistory_47.save()

    south_migrationhistory_48 = MigrationHistory()
    south_migrationhistory_48.app_name = u'filer'
    south_migrationhistory_48.migration = u'0005_auto__add_field_file_sha1__chg_field_file_file'
    south_migrationhistory_48.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 333522, tzinfo=utc)
    south_migrationhistory_48.save()

    south_migrationhistory_49 = MigrationHistory()
    south_migrationhistory_49.app_name = u'filer'
    south_migrationhistory_49.migration = u'0006_polymorphic__add_field_file_polymorphic_ctype'
    south_migrationhistory_49.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 341883, tzinfo=utc)
    south_migrationhistory_49.save()

    south_migrationhistory_50 = MigrationHistory()
    south_migrationhistory_50.app_name = u'filer'
    south_migrationhistory_50.migration = u'0007_polymorphic__content_type_data'
    south_migrationhistory_50.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 350797, tzinfo=utc)
    south_migrationhistory_50.save()

    south_migrationhistory_51 = MigrationHistory()
    south_migrationhistory_51.app_name = u'filer'
    south_migrationhistory_51.migration = u'0008_polymorphic__del_field_file__file_type_plugin_name'
    south_migrationhistory_51.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 359162, tzinfo=utc)
    south_migrationhistory_51.save()

    south_migrationhistory_52 = MigrationHistory()
    south_migrationhistory_52.app_name = u'filer'
    south_migrationhistory_52.migration = u'0009_auto__add_field_folderpermission_can_edit_new__add_field_folderpermiss'
    south_migrationhistory_52.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 367629, tzinfo=utc)
    south_migrationhistory_52.save()

    south_migrationhistory_53 = MigrationHistory()
    south_migrationhistory_53.app_name = u'filer'
    south_migrationhistory_53.migration = u'0010_folderpermissions'
    south_migrationhistory_53.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 377069, tzinfo=utc)
    south_migrationhistory_53.save()

    south_migrationhistory_54 = MigrationHistory()
    south_migrationhistory_54.app_name = u'filer'
    south_migrationhistory_54.migration = u'0011_auto__del_field_folderpermission_can_add_children__del_field_folderper'
    south_migrationhistory_54.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 385476, tzinfo=utc)
    south_migrationhistory_54.save()

    south_migrationhistory_55 = MigrationHistory()
    south_migrationhistory_55.app_name = u'filer'
    south_migrationhistory_55.migration = u'0012_renaming_folderpermissions'
    south_migrationhistory_55.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 393607, tzinfo=utc)
    south_migrationhistory_55.save()

    south_migrationhistory_56 = MigrationHistory()
    south_migrationhistory_56.app_name = u'easy_thumbnails'
    south_migrationhistory_56.migration = u'0001_initial'
    south_migrationhistory_56.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 442502, tzinfo=utc)
    south_migrationhistory_56.save()

    south_migrationhistory_57 = MigrationHistory()
    south_migrationhistory_57.app_name = u'easy_thumbnails'
    south_migrationhistory_57.migration = u'0002_filename_indexes'
    south_migrationhistory_57.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 449785, tzinfo=utc)
    south_migrationhistory_57.save()

    south_migrationhistory_58 = MigrationHistory()
    south_migrationhistory_58.app_name = u'easy_thumbnails'
    south_migrationhistory_58.migration = u'0003_auto__add_storagenew'
    south_migrationhistory_58.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 458186, tzinfo=utc)
    south_migrationhistory_58.save()

    south_migrationhistory_59 = MigrationHistory()
    south_migrationhistory_59.app_name = u'easy_thumbnails'
    south_migrationhistory_59.migration = u'0004_auto__add_field_source_storage_new__add_field_thumbnail_storage_new'
    south_migrationhistory_59.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 465904, tzinfo=utc)
    south_migrationhistory_59.save()

    south_migrationhistory_60 = MigrationHistory()
    south_migrationhistory_60.app_name = u'easy_thumbnails'
    south_migrationhistory_60.migration = u'0005_storage_fks_null'
    south_migrationhistory_60.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 475269, tzinfo=utc)
    south_migrationhistory_60.save()

    south_migrationhistory_61 = MigrationHistory()
    south_migrationhistory_61.app_name = u'easy_thumbnails'
    south_migrationhistory_61.migration = u'0006_copy_storage'
    south_migrationhistory_61.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 483553, tzinfo=utc)
    south_migrationhistory_61.save()

    south_migrationhistory_62 = MigrationHistory()
    south_migrationhistory_62.app_name = u'easy_thumbnails'
    south_migrationhistory_62.migration = u'0007_storagenew_fks_not_null'
    south_migrationhistory_62.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 491689, tzinfo=utc)
    south_migrationhistory_62.save()

    south_migrationhistory_63 = MigrationHistory()
    south_migrationhistory_63.app_name = u'easy_thumbnails'
    south_migrationhistory_63.migration = u'0008_auto__del_field_source_storage__del_field_thumbnail_storage'
    south_migrationhistory_63.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 499850, tzinfo=utc)
    south_migrationhistory_63.save()

    south_migrationhistory_64 = MigrationHistory()
    south_migrationhistory_64.app_name = u'easy_thumbnails'
    south_migrationhistory_64.migration = u'0009_auto__del_storage'
    south_migrationhistory_64.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 509955, tzinfo=utc)
    south_migrationhistory_64.save()

    south_migrationhistory_65 = MigrationHistory()
    south_migrationhistory_65.app_name = u'easy_thumbnails'
    south_migrationhistory_65.migration = u'0010_rename_storage'
    south_migrationhistory_65.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 521338, tzinfo=utc)
    south_migrationhistory_65.save()

    south_migrationhistory_66 = MigrationHistory()
    south_migrationhistory_66.app_name = u'easy_thumbnails'
    south_migrationhistory_66.migration = u'0011_auto__add_field_source_storage_hash__add_field_thumbnail_storage_hash'
    south_migrationhistory_66.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 529732, tzinfo=utc)
    south_migrationhistory_66.save()

    south_migrationhistory_67 = MigrationHistory()
    south_migrationhistory_67.app_name = u'easy_thumbnails'
    south_migrationhistory_67.migration = u'0012_build_storage_hashes'
    south_migrationhistory_67.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 538280, tzinfo=utc)
    south_migrationhistory_67.save()

    south_migrationhistory_68 = MigrationHistory()
    south_migrationhistory_68.app_name = u'easy_thumbnails'
    south_migrationhistory_68.migration = u'0013_auto__del_storage__del_field_source_storage__del_field_thumbnail_stora'
    south_migrationhistory_68.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 551059, tzinfo=utc)
    south_migrationhistory_68.save()

    south_migrationhistory_69 = MigrationHistory()
    south_migrationhistory_69.app_name = u'easy_thumbnails'
    south_migrationhistory_69.migration = u'0014_auto__add_unique_source_name_storage_hash__add_unique_thumbnail_name_s'
    south_migrationhistory_69.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 558141, tzinfo=utc)
    south_migrationhistory_69.save()

    south_migrationhistory_70 = MigrationHistory()
    south_migrationhistory_70.app_name = u'easy_thumbnails'
    south_migrationhistory_70.migration = u'0015_auto__del_unique_thumbnail_name_storage_hash__add_unique_thumbnail_sou'
    south_migrationhistory_70.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 565204, tzinfo=utc)
    south_migrationhistory_70.save()

    south_migrationhistory_71 = MigrationHistory()
    south_migrationhistory_71.app_name = u'cmsplugin_nivoslider'
    south_migrationhistory_71.migration = u'0001_initial'
    south_migrationhistory_71.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 619047, tzinfo=utc)
    south_migrationhistory_71.save()

    south_migrationhistory_72 = MigrationHistory()
    south_migrationhistory_72.app_name = u'cmsplugin_nivoslider'
    south_migrationhistory_72.migration = u'0002_auto__add_field_sliderplugin_theme__add_field_sliderplugin_effect'
    south_migrationhistory_72.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 627650, tzinfo=utc)
    south_migrationhistory_72.save()

    south_migrationhistory_73 = MigrationHistory()
    south_migrationhistory_73.app_name = u'cmsplugin_nivoslider'
    south_migrationhistory_73.migration = u'0003_auto__add_field_sliderplugin_anim_speed__add_field_sliderplugin_pause_'
    south_migrationhistory_73.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 636130, tzinfo=utc)
    south_migrationhistory_73.save()

    south_migrationhistory_74 = MigrationHistory()
    south_migrationhistory_74.app_name = u'cmsplugin_nivoslider'
    south_migrationhistory_74.migration = u'0004_auto__add_field_sliderplugin_image_width__add_field_sliderplugin_image'
    south_migrationhistory_74.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 645708, tzinfo=utc)
    south_migrationhistory_74.save()

    south_migrationhistory_75 = MigrationHistory()
    south_migrationhistory_75.app_name = u'cmsplugin_nivoslider'
    south_migrationhistory_75.migration = u'0005_auto__add_field_sliderplugin_show_ribbon'
    south_migrationhistory_75.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 655252, tzinfo=utc)
    south_migrationhistory_75.save()

    south_migrationhistory_76 = MigrationHistory()
    south_migrationhistory_76.app_name = u'cmsplugin_nivoslider'
    south_migrationhistory_76.migration = u'0006_rename_fields_image_height_width__del_field_show_ribbon'
    south_migrationhistory_76.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 663417, tzinfo=utc)
    south_migrationhistory_76.save()

    south_migrationhistory_77 = MigrationHistory()
    south_migrationhistory_77.app_name = u'cmsplugin_nivoslider'
    south_migrationhistory_77.migration = u'0007_auto__add_field_sliderplugin_manual_advance__add_field_sliderplugin_ar'
    south_migrationhistory_77.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 671610, tzinfo=utc)
    south_migrationhistory_77.save()

    south_migrationhistory_78 = MigrationHistory()
    south_migrationhistory_78.app_name = u'cmsplugin_nivoslider'
    south_migrationhistory_78.migration = u'0008_auto__del_sliderimage__del_slideralbum'
    south_migrationhistory_78.applied = datetime.datetime(2012, 8, 29, 11, 29, 40, 679663, tzinfo=utc)
    south_migrationhistory_78.save()

    south_migrationhistory_79 = MigrationHistory()
    south_migrationhistory_79.app_name = u'myforms'
    south_migrationhistory_79.migration = u'0001_initial'
    south_migrationhistory_79.applied = datetime.datetime(2012, 8, 29, 11, 46, 15, 239210, tzinfo=utc)
    south_migrationhistory_79.save()

    south_migrationhistory_80 = MigrationHistory()
    south_migrationhistory_80.app_name = u'myforms'
    south_migrationhistory_80.migration = u'0002_auto__add_field_formlog_date'
    south_migrationhistory_80.applied = datetime.datetime(2012, 8, 29, 11, 47, 8, 213751, tzinfo=utc)
    south_migrationhistory_80.save()

    south_migrationhistory_81 = MigrationHistory()
    south_migrationhistory_81.app_name = u'menu'
    south_migrationhistory_81.migration = u'0001_initial'
    south_migrationhistory_81.applied = datetime.datetime(2012, 8, 29, 12, 31, 45, 106875, tzinfo=utc)
    south_migrationhistory_81.save()

    south_migrationhistory_82 = MigrationHistory()
    south_migrationhistory_82.app_name = u'menu'
    south_migrationhistory_82.migration = u'0002_initial'
    south_migrationhistory_82.applied = datetime.datetime(2012, 8, 29, 12, 31, 51, 567025, tzinfo=utc)
    south_migrationhistory_82.save()

    south_migrationhistory_83 = MigrationHistory()
    south_migrationhistory_83.app_name = u'dashboard'
    south_migrationhistory_83.migration = u'0001_initial'
    south_migrationhistory_83.applied = datetime.datetime(2012, 8, 29, 12, 32, 44, 447764, tzinfo=utc)
    south_migrationhistory_83.save()

    south_migrationhistory_84 = MigrationHistory()
    south_migrationhistory_84.app_name = u'dashboard'
    south_migrationhistory_84.migration = u'0002_auto__add_field_dashboardpreferences_dashboard_id'
    south_migrationhistory_84.applied = datetime.datetime(2012, 8, 29, 12, 32, 44, 595134, tzinfo=utc)
    south_migrationhistory_84.save()

    south_migrationhistory_85 = MigrationHistory()
    south_migrationhistory_85.app_name = u'dashboard'
    south_migrationhistory_85.migration = u'0003_initial'
    south_migrationhistory_85.applied = datetime.datetime(2012, 8, 29, 12, 32, 57, 389686, tzinfo=utc)
    south_migrationhistory_85.save()

    from menus.models import CacheKey

    menus_cachekey_1 = CacheKey()
    menus_cachekey_1.language = u'ru'
    menus_cachekey_1.site = 1
    menus_cachekey_1.key = u'cms-menu_nodes_ru_1_1_user'
    menus_cachekey_1.save()

    menus_cachekey_2 = CacheKey()
    menus_cachekey_2.language = u'ru'
    menus_cachekey_2.site = 1
    menus_cachekey_2.key = u'cms-menu_nodes_ru_1'
    menus_cachekey_2.save()

    from cms.plugins.text.models import Text

    cmsplugin_text_1 = Text()
    cmsplugin_text_1.placeholder = cms_placeholder_2
    cmsplugin_text_1.parent = None
    cmsplugin_text_1.position = 0
    cmsplugin_text_1.language = u'ru'
    cmsplugin_text_1.plugin_type = u'TextPlugin'
    cmsplugin_text_1.creation_date = datetime.datetime(2012, 8, 30, 11, 3, 56, 633476, tzinfo=utc)
    cmsplugin_text_1.level = 0
    cmsplugin_text_1.lft = 1
    cmsplugin_text_1.rght = 2
    cmsplugin_text_1.tree_id = 2
    cmsplugin_text_1.body = u'<h2>\u041f\u0440\u0438\u043e\u0431\u0440\u0435\u0442\u0438\u0442\u0435 \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u043e\u0432\u0430\u0440.</h2>\n<p>\u041f\u0440\u044f\u043c\u043e \u0441\u0435\u0439\u0447\u0430\u0441 \u0443 \u0432\u0430\u0441 \u043f\u043e\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u0438\u043e\u0431\u0440\u0435\u0441\u0442\u0438 \u044d\u0442\u043e\u0442 \u0442\u043e\u0432\u0430\u0440, \u0442\u043e\u043b\u044c\u043a\u043e \u0443 \u043d\u0430\u0441. \u0412\u044b \u043a\u043e\u0433\u0434\u0430-\u043d\u0438\u0431\u0443\u0434\u044c \u043f\u0440\u0438\u0445\u043e\u0434\u0438\u043b\u0438 \u0434\u043e\u043c\u043e\u0439 \u043f\u0440\u043e\u043c\u043e\u043a\u0448\u0438\u0435 \u0434\u043e \u043d\u0438\u0442\u043a\u0438? \u0412\u0430\u0441 \u043a\u043e\u0433\u0434\u0430-\u043d\u0438\u0431\u0443\u0434\u044c \u0437\u0430\u0441\u0442\u0430\u0432\u0430\u043b \u0432 \u0432\u0440\u0430\u0441\u043f\u043b\u043e\u0445 \u0432\u043d\u0435\u0437\u0430\u043f\u043d\u043e \u043d\u0430\u0447\u0430\u0432\u0448\u0438\u0439\u0441\u044f \u0434\u043e\u0436\u0434\u044c? \u0412\u044b \u0431\u044b \u0445\u043e\u0442\u0435\u043b\u0438 \u0432\u0441\u0435\u0433\u0434\u0430 \u0438\u043c\u0435\u0442\u044c \u043f\u0440\u0438 \u0441\u0435\u0431\u0435 \u0441\u0442\u0438\u043b\u044c\u043d\u044b\u0439, \u043c\u043e\u0434\u043d\u044b\u0439 \u0437\u043e\u043d\u0442, \u043f\u043e\u0434\u0447\u0435\u0440\u043a\u0438\u0432\u0430\u044e\u0449\u0438\u0439 \u0432\u0430\u0448\u0443 \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c?</p>\n<h2>\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0437\u043e\u043d\u0442 \u043f\u043e \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0439 \u0446\u0435\u043d\u0435.</h2>\n<p>\u0415\u0441\u043b\u0438 \u0432\u044b \u043e\u0442\u0432\u0435\u0442\u0438\u043b\u0438 \u0434\u0430, \u0442\u043e \u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u043f\u0440\u0438\u043e\u0431\u0440\u0435\u0441\u0442\u0438 \u0443 \u043d\u0430\u0441 \u0441\u0432\u0435\u0440\u0445 \u043f\u0440\u043e\u0447\u043d\u044b\u0439 \u0437\u043e\u043d\u0442 \u0441 \u0441\u0438\u0441\u0442\u0435\u043c\u043e\u0439 \u0430\u043d\u0442\u0438-\u0448\u0442\u043e\u0440\u043c. \u042d\u0442\u043e\u0442 \u0437\u043e\u043d\u0442 \u043f\u043e\u043c\u043e\u0436\u0435\u0442 \u0432\u0430\u043c \u043f\u0440\u0438\u0439\u0442\u0438 \u0434\u043e\u043c\u043e\u0439 \u043d\u0435 \u043f\u0440\u043e\u043c\u043e\u043a\u043d\u0443\u0432 \u0432\u043e \u0432\u0440\u0435\u043c\u044f \u0441\u0438\u043b\u044c\u043d\u043e\u0433\u043e \u043b\u0438\u0432\u043d\u044f. \u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u043f\u0438\u0446\u044b \u0441 \u0443\u0441\u0438\u043b\u0435\u043d\u043d\u043e\u0439 \u043f\u043b\u0430\u0441\u0442\u0438\u043a\u043e\u0432\u043e\u0439 \u043e\u043f\u043e\u0440\u043e\u0439, \u043c\u0435\u043d\u044c\u0448\u0435 \u043f\u043e\u0434\u0432\u0435\u0440\u0436\u0435\u043d\u044b \u0440\u0436\u0430\u0432\u0447\u0438\u043d\u0435 \u0438 \u043a\u043e\u0440\u0440\u043e\u0437\u0438\u0438. \u042d\u0442\u043e\u0442 \u043f\u0440\u043e\u0434\u0443\u043a\u0442 \u0431\u0443\u0434\u0435\u0442 \u0432\u0435\u0440\u043d\u044b\u043c \u0434\u0440\u0443\u0433\u043e\u043c \u0438 \u0441\u043f\u0430\u0441\u0438\u0442\u0435\u043b\u0435\u043c, \u0432 \u0434\u043e\u0436\u0434\u043b\u0438\u0432\u044b\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u0430 \u0433\u043e\u0434\u0430. \u042d\u0442\u043e\u0442 \u0437\u043e\u043d\u0442 \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043b\u0438\u0447\u043d\u044b\u0439 \u0434\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435\u043c \u043a \u0432\u0430\u0448\u0435\u043c\u0443 \u0441\u0442\u0438\u043b\u044e \u0438 \u043f\u043e\u043c\u043e\u0436\u0435\u0442 \u043f\u043e\u0434\u0447\u0435\u0440\u043a\u043d\u0443\u0442\u044c \u0432\u0430\u0448\u0443 \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c.</p>\n<h2>\u041a\u0443\u043f\u0438 \u0443 \u043d\u0430\u0441.</h2>\n<p>\u041f\u043e\u043a\u0443\u043f\u0430\u0439\u0442\u0435 \u0437\u043e\u043d\u0442 \u043f\u0440\u044f\u043c\u043e \u0441\u0435\u0439\u0447\u0430\u0441, \u043d\u0435 \u0443\u043f\u0443\u0441\u0442\u0438\u0442\u0435 \u0442\u0430\u043a\u0443\u044e \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c.</p>'
    cmsplugin_text_1.save()

    cmsplugin_text_2 = Text()
    cmsplugin_text_2.placeholder = cms_placeholder_6
    cmsplugin_text_2.parent = None
    cmsplugin_text_2.position = 0
    cmsplugin_text_2.language = u'ru'
    cmsplugin_text_2.plugin_type = u'TextPlugin'
    cmsplugin_text_2.creation_date = datetime.datetime(2012, 8, 30, 11, 15, 41, 337271, tzinfo=utc)
    cmsplugin_text_2.level = 0
    cmsplugin_text_2.lft = 1
    cmsplugin_text_2.rght = 2
    cmsplugin_text_2.tree_id = 4
    cmsplugin_text_2.body = u'<h2>\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430</h2>\n<p>\u041c\u044b \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0443\u0435\u043c \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0443 \u043f\u043e \u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433\u0443 \u0438 \u0432\u0441\u0435\u0439 \u0420\u043e\u0441\u0441\u0438\u0438.<br/> \u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438 \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 250 \u0440\u0443\u0431.</p>'
    cmsplugin_text_2.save()

    cmsplugin_text_3 = Text()
    cmsplugin_text_3.placeholder = cms_placeholder_8
    cmsplugin_text_3.parent = None
    cmsplugin_text_3.position = 0
    cmsplugin_text_3.language = u'ru'
    cmsplugin_text_3.plugin_type = u'TextPlugin'
    cmsplugin_text_3.creation_date = datetime.datetime(2012, 8, 30, 11, 16, 44, 432103, tzinfo=utc)
    cmsplugin_text_3.level = 0
    cmsplugin_text_3.lft = 1
    cmsplugin_text_3.rght = 2
    cmsplugin_text_3.tree_id = 5
    cmsplugin_text_3.body = u'<h2>\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b</h2>\n<p><br/><br/></p>\n<p>\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u0434\u043b\u044f \u0441\u0432\u044f\u0437\u0438:<span style="font-size: 22px; color: #ff0000;"> (812) 920-62-12</span></p>\n<p>\u0422\u0430\u043a \u0436\u0435 \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u043d\u0430\u043c \u043d\u0430\u043f\u0438\u0441\u0430\u0442\u044c <a href="../../../../../../../zakazat/">\u043f\u0438\u0441\u044c\u043c\u043e \u043f\u0440\u044f\u043c\u043e \u0441 \u0441\u0430\u0439\u0442\u0430</a>.<br/> \u0418\u043b\u0438 \u043f\u043e \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u0435 \u043d\u0430 \u0430\u0434\u0440\u0435\u0441: <span style="color: #0000ff; font-size: 20px;">sale@mega-zont.ru</span></p>\n<p>\u041d\u0430\u0448 \u0430\u0434\u0440\u0435\u0441:</p>\n<address>\u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433, \u0443\u043b\u0438\u0446\u0430 \u0413\u043e\u0440\u043e\u0445\u043e\u0432\u0430\u044f, \u0434\u043e\u043c 49, \u043d\u0435\u0434\u0430\u043b\u0435\u043a\u043e \u043e\u0442 \u0441\u0442\u0430\u043d\u0446\u0438\u0438 \u043c\u0435\u0442\u0440\u043e \u0421\u0435\u043d\u043d\u0430\u044f.</address>'
    cmsplugin_text_3.save()

    cmsplugin_text_4 = Text()
    cmsplugin_text_4.placeholder = cms_placeholder_10
    cmsplugin_text_4.parent = None
    cmsplugin_text_4.position = 0
    cmsplugin_text_4.language = u'ru'
    cmsplugin_text_4.plugin_type = u'TextPlugin'
    cmsplugin_text_4.creation_date = datetime.datetime(2012, 8, 30, 11, 20, 5, 572834, tzinfo=utc)
    cmsplugin_text_4.level = 0
    cmsplugin_text_4.lft = 1
    cmsplugin_text_4.rght = 2
    cmsplugin_text_4.tree_id = 6
    cmsplugin_text_4.body = u'<h2>\u041e\u043f\u0442\u043e\u0432\u044b\u0435 \u0437\u0430\u043a\u0443\u043f\u043a\u0438</h2>\n<p>\u0423 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u0438\u043e\u0431\u0440\u0435\u0441\u0442\u0438 \u043d\u0430\u0448\u0438 \u0437\u043e\u043d\u0442\u044b \u043f\u043e \u043e\u043f\u0442\u043e\u0432\u044b\u043c \u0446\u0435\u043d\u0430\u043c. \u041e\u043f\u0442\u043e\u043c \u0441\u0447\u0438\u0442\u0430\u0435\u0442\u0441\u044f \u043f\u0430\u0440\u0442\u0438\u044f \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043e\u0432\u0430\u0440\u0430 \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043e\u0442 20 \u0448\u0442\u0443\u043a. \u041c\u044b \u043d\u0430\u0439\u0434\u0435\u043c \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u043e\u0434\u0445\u043e\u0434 \u043a \u043a\u0430\u0436\u0434\u043e\u043c\u0443, <a href="../../../../../../../kontakty/">\u0437\u0432\u043e\u043d\u0438\u0442\u0435 \u043d\u0430\u043c</a> \u0438\u043b\u0438 <a href="../../../../../../../zakazat/">\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0439\u0442\u0435 \u0437\u0430\u044f\u0432\u043a\u0443</a> \u043d\u0430 \u0441\u0430\u0439\u0442\u0435.</p>'
    cmsplugin_text_4.save()

    from bootstrap_tags.models import ClearHtml

    cmsplugin_clearhtml_1 = ClearHtml()
    cmsplugin_clearhtml_1.placeholder = cms_placeholder_2
    cmsplugin_clearhtml_1.parent = None
    cmsplugin_clearhtml_1.position = 1
    cmsplugin_clearhtml_1.language = u'ru'
    cmsplugin_clearhtml_1.plugin_type = u'ClearHtmlPlugin'
    cmsplugin_clearhtml_1.creation_date = datetime.datetime(2012, 8, 30, 11, 12, 9, 307947, tzinfo=utc)
    cmsplugin_clearhtml_1.level = 0
    cmsplugin_clearhtml_1.lft = 1
    cmsplugin_clearhtml_1.rght = 2
    cmsplugin_clearhtml_1.tree_id = 3
    cmsplugin_clearhtml_1.text_f = u'<a href="/zakazat/" class=\'btn btn-primary btn-large\'><i class="icon-shopping-cart icon-white"></i> \u041a\u0443\u043f\u0438\u0442\u044c</a>'
    cmsplugin_clearhtml_1.save()

    from filer.models.foldermodels import Folder


    from filer.models.foldermodels import FolderPermission


    from filer.models.filemodels import File


    from filer.models.clipboardmodels import Clipboard


    from filer.models.clipboardmodels import ClipboardItem


    from filer.models.imagemodels import Image


    from easy_thumbnails.models import Source


    from easy_thumbnails.models import Thumbnail


    from cmsplugin_nivoslider.models import SliderPlugin


    from myforms.models import FormLogPlugin

    cmsplugin_formlogplugin_1 = FormLogPlugin()
    cmsplugin_formlogplugin_1.placeholder = cms_placeholder_4
    cmsplugin_formlogplugin_1.parent = None
    cmsplugin_formlogplugin_1.position = 0
    cmsplugin_formlogplugin_1.language = u'ru'
    cmsplugin_formlogplugin_1.plugin_type = u'MyFormPlugin'
    cmsplugin_formlogplugin_1.creation_date = datetime.datetime(2012, 8, 29, 11, 30, 31, 24751, tzinfo=utc)
    cmsplugin_formlogplugin_1.level = 0
    cmsplugin_formlogplugin_1.lft = 1
    cmsplugin_formlogplugin_1.rght = 2
    cmsplugin_formlogplugin_1.tree_id = 1
    cmsplugin_formlogplugin_1.form_number = 1
    cmsplugin_formlogplugin_1.save()

    from myforms.models import FormLog

    myforms_formlog_1 = FormLog()
    myforms_formlog_1.email = u'koligin@mail.ru'
    myforms_formlog_1.comment = u'546456'
    myforms_formlog_1.date = datetime.datetime(2012, 8, 28, 20, 0, tzinfo=utc)
    myforms_formlog_1.save()

    myforms_formlog_2 = FormLog()
    myforms_formlog_2.email = u'koligin345345@mail.ru'
    myforms_formlog_2.comment = u'345345345'
    myforms_formlog_2.date = datetime.datetime(2012, 8, 29, 11, 48, 8, 902154, tzinfo=utc)
    myforms_formlog_2.save()

    myforms_formlog_3 = FormLog()
    myforms_formlog_3.email = u'koligin@mail.ru'
    myforms_formlog_3.comment = u'345'
    myforms_formlog_3.date = datetime.datetime(2012, 8, 30, 12, 17, 16, 148758, tzinfo=utc)
    myforms_formlog_3.save()

    from options.models import Options

    options_options_1 = Options()
    options_options_1.name = u'kuponator'
    options_options_1.status_text = u''
    options_options_1.status_bool = False
    options_options_1.discription = u'\u0411\u0443\u043b\u0435\u0432\u043d\u043e\u0435 \u0437\u0430\u043d\u0447\u0435\u043d\u0438\u0435, \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442 \u0440\u0435\u0436\u0438\u043c \u043a\u0443\u043f\u043e\u043d\u0430\u0442\u043e\u0440 \u0438\u043b\u0438 \u043d\u0435\u0442'
    options_options_1.save()

    from admin_tools.menu.models import Bookmark


    from admin_tools.dashboard.models import DashboardPreferences

    admin_tools_dashboard_preferences_1 = DashboardPreferences()
    admin_tools_dashboard_preferences_1.user = auth_user_1
    admin_tools_dashboard_preferences_1.data = u'{}'
    admin_tools_dashboard_preferences_1.dashboard_id = u'dashboard'
    admin_tools_dashboard_preferences_1.save()

