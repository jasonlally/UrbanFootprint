# UrbanFootprint-California, Scenario Planning Model
# 
# Copyright (C) 2012-2013 Calthorpe Associates
# 
# This program is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, version 3 of the License.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
# 
# Contact: Calthorpe Associates (urbanfootprint@calthorpe.com)
# Firm contact: 2095 Rose Street Suite 201, Berkeley CA 94709.
# Phone: (510) 548-6800.      Web: www.calthorpe.com
# 

#
# 

#
# 

# coding=utf-8
#

from django.db import models
from footprint.models.geospatial.feature import Feature

__author__ = 'calthorpe'

class DevelopableFeature(Feature):
    acres_gross = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    acres_developable = models.DecimalField(max_digits=14, decimal_places=4)
    acres_urban = models.DecimalField(max_digits=14, decimal_places=4)
    acres_greenfield = models.DecimalField(max_digits=14, decimal_places=4)
    acres_constrained = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_res = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_res_detsf = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_res_detsf_ll = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_res_detsf_sl = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_res_attsf = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_res_mf = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_emp = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_emp_ret = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_emp_off = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_emp_ind = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_emp_ag = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_emp_mixed = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_emp_military = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_mixed = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_mixed_w_off = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_mixed_no_off = models.DecimalField(max_digits=14, decimal_places=4)
    acres_parcel_no_use = models.DecimalField(max_digits=14, decimal_places=4)

    pop = models.DecimalField(max_digits=14, decimal_places=4)
    hh = models.DecimalField(max_digits=14, decimal_places=4)
    du = models.DecimalField(max_digits=14, decimal_places=4)
    du_detsf = models.DecimalField(max_digits=14, decimal_places=4)
    du_detsf_ll = models.DecimalField(max_digits=14, decimal_places=4)
    du_detsf_sl = models.DecimalField(max_digits=14, decimal_places=4)
    du_attsf = models.DecimalField(max_digits=14, decimal_places=4)
    du_mf = models.DecimalField(max_digits=14, decimal_places=4)

    emp = models.DecimalField(max_digits=14, decimal_places=4)
    emp_ret = models.DecimalField(max_digits=14, decimal_places=4)
    emp_retail_services = models.DecimalField(max_digits=14, decimal_places=4)
    emp_restaurant = models.DecimalField(max_digits=14, decimal_places=4)
    emp_accommodation = models.DecimalField(max_digits=14, decimal_places=4)
    emp_arts_entertainment = models.DecimalField(max_digits=14, decimal_places=4)
    emp_other_services = models.DecimalField(max_digits=14, decimal_places=4)
    emp_off = models.DecimalField(max_digits=14, decimal_places=4)
    emp_office_services = models.DecimalField(max_digits=14, decimal_places=4)
    emp_education = models.DecimalField(max_digits=14, decimal_places=4)
    emp_public_admin = models.DecimalField(max_digits=14, decimal_places=4)
    emp_medical_services = models.DecimalField(max_digits=14, decimal_places=4)

    emp_ind = models.DecimalField(max_digits=14, decimal_places=4)
    emp_wholesale = models.DecimalField(max_digits=14, decimal_places=4)
    emp_transport_warehousing = models.DecimalField(max_digits=14, decimal_places=4)
    emp_manufacturing = models.DecimalField(max_digits=14, decimal_places=4)
    emp_utilities = models.DecimalField(max_digits=14, decimal_places=4)
    emp_construction = models.DecimalField(max_digits=14, decimal_places=4)
    emp_ag = models.DecimalField(max_digits=14, decimal_places=4)
    emp_agriculture = models.DecimalField(max_digits=14, decimal_places=4)
    emp_extraction = models.DecimalField(max_digits=14, decimal_places=4)
    emp_military = models.DecimalField(max_digits=14, decimal_places=4)

    bldg_sqft_detsf_ll = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_detsf_sl = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_attsf = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_mf = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_retail_services = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_restaurant = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_accommodation = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_arts_entertainment = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_other_services = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_office_services = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_public_admin = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_medical_services = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_education = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_wholesale = models.DecimalField(max_digits=14, decimal_places=4)
    bldg_sqft_transport_warehousing = models.DecimalField(max_digits=14, decimal_places=4)

    commercial_irrigated_sqft = models.DecimalField(max_digits=14, decimal_places=4)
    residential_irrigated_sqft = models.DecimalField(max_digits=14, decimal_places=4)

    hh_inc_00_10 = models.DecimalField(max_digits=14, decimal_places=4)
    hh_inc_10_20 = models.DecimalField(max_digits=14, decimal_places=4)
    hh_inc_20_30 = models.DecimalField(max_digits=14, decimal_places=4)
    hh_inc_30_40 = models.DecimalField(max_digits=14, decimal_places=4)
    hh_inc_40_50 = models.DecimalField(max_digits=14, decimal_places=4)
    hh_inc_50_60 = models.DecimalField(max_digits=14, decimal_places=4)
    hh_inc_60_75 = models.DecimalField(max_digits=14, decimal_places=4)
    hh_inc_75_100 = models.DecimalField(max_digits=14, decimal_places=4)
    hh_inc_100_125 = models.DecimalField(max_digits=14, decimal_places=4)
    hh_inc_125_150 = models.DecimalField(max_digits=14, decimal_places=4)
    hh_inc_150_200 = models.DecimalField(max_digits=14, decimal_places=4)
    hh_inc_200p = models.DecimalField(max_digits=14, decimal_places=4)
    hh_agg_inc = models.DecimalField(max_digits=14, decimal_places=4)
    hh_owner_occ = models.DecimalField(max_digits=14, decimal_places=4)
    hh_rental_occ = models.DecimalField(max_digits=14, decimal_places=4)

    def __unicode__(self):
        return unicode("Dev Acres config for %s" % self.scenario.name)

    class Meta(object):
        abstract = True
        app_label = 'footprint'


class TemplateDevelopableFeature(DevelopableFeature):
    """
        Template subclass so that south generates migrations that we can apply to the dynamically generated subclasses
    """

    class Meta(object):
        app_label = 'footprint'
        abstract = False
