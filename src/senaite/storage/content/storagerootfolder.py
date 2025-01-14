# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.STORAGE.
#
# SENAITE.STORAGE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2019-2022 by it's authors.
# Some rights reserved, see README and LICENSE.

from bika.lims.content.bikaschema import BikaFolderSchema
from plone.app.folder.folder import ATFolder
from Products.Archetypes.atapi import registerType
from senaite.core.interfaces import IHideActionsMenu
from senaite.storage import PRODUCT_NAME
from senaite.storage.interfaces import IStorageRootFolder
from zope.interface import implements

schema = BikaFolderSchema.copy()


class StorageRootFolder(ATFolder):
    """Storage module root object
    """
    implements(IStorageRootFolder, IHideActionsMenu)
    displayContentsTab = False
    schema = schema


registerType(StorageRootFolder, PRODUCT_NAME)
