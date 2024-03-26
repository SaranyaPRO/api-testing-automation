class LoginPageLocators:
    MOBILENUMBER_FIELD = "//input[@title='Enter Phone Number']"
    PROD_MOBILENUMBER_FIELD = "//input[@id='phoneNumber']"
    LOGIN_CONTINUE_BUTTON = "//button[@id='continue']"
    PROD_LOGIN_CONTINUE_BUTTON = "//button[@id='next']"
    LOGIN_CANCEL_BUTTON = "//div[@class='buttons']//button[@id='cancel']"
    OTP_FIELD = "//input[@id='verificationCode']"


class NavigationBarLocators:
    USER_PROFILE_ICON = "//button//img[@class='profile-icon']"
    NAV_PROJECTS = "//li[@class='nav-item']//a[text()=' Projects ']"
    NAV_UPDATED_INFOR = "//li[@class='nav-item']//a[text()=' Updated Info ']"
    NAV_MASTER_DATA = (
        "//li[@class='nav-item']//a[normalize-space(text())='Master data']"
    )
    USER_NAME_PLACE = "//div[@class='right']//li[1]"
    ACTIVE_NAVIGATION_BAR = "//a[@class='nav-link active']"


class ProjectPageLocators:
    SUMMARY_LABEL = "//h5[normalize-space(text())='Summary']"
    NAME_LIST_PROJECTLIST = "//th[normalize-space(text())='Name']"
    PROJECT_SEARCH_FIELD = (
        "//div[@class='search']//div//input[@placeholder='Project name filter']"
    )
    PROJECT_NAME_BREADCRUMB = "(//div[@class='container']//div)[2]//span"
    FORM_SEARCH_FIELD = "//input[@placeholder='Search']"
    ACTIVE_SUBDEPARTMENT_NAME = (
        "//li[@class='subDepartment ng-star-inserted active']//a"
    )
    PROJECT_LIST_COLUMN_NAME = (
        "//table[@aria-describedby='users']//th[normalize-space(text())='Name']"
    )


class InputFormEntryPageLocators:
    FORM_ADD_NEW_BUTTON = "//button[normalize-space(text())='Add New']"
    FORM_HEADER_VALUE = "//h5[text()]"
    SUBMIT_BUTTON = "//button[normalize-space(text())='Submit']"
    FIRST_COLUMN_VALUE = "//td[normalize-space(text())='1']//..//td[3]//p"
    FORM_RESPONSE_COUNT = "//table[@aria-describedby='Form Response table']//tbody//tr"
    EXTERNALAPI_INPUTFORM_NODATAFOUND = (
        "//tfoot//tr//th[normalize-space(text())='No Data Found.']"
    )


class InpurFormCreationLocators:
    CREATE_FORM_BUTTON = "//div[@class='search-container d-flex']//button[normalize-space(text())='Create Form']"
    CREATE_FORM_LABEL = "//h4[normalize-space(text())='Create form']"
    USE_EXISTINGFORM_CHECKBOX = "//span[normalize-space(text())='Use existing form']//..//input[@type='checkbox']"
    COPY_FORM_CHECKBOX = "//span[normalize-space(text())='copy form']//..//input[@class='form-check-input']"
    COPY_FORM_CHECKBOX_IFCHECKED = (
        "//span[normalize-space(text())='copy form']//..//input[@checked='true']"
    )
    ENTER_NEW_FORM_NAME_FIELD = (
        "//label[normalize-space(text())='Enter new Form name']//..//div//input"
    )
    CHOOSE_FORM_TYPE_SELECT = "//label[normalize-space(text())='Choose Form type']//..//div[@class='choices form-group formio-choices']"
    CHOOSE_FORM_TYPE_INPUTFORM = "//label[normalize-space(text())='Choose Form type']//..//div[@class='choices__list choices__list--dropdown is-active']//div[@class='choices__list']//div//span[normalize-space(text())='inputForm']"
    INPUT_FORM_OPTION_LIST = (
        "//div[@role='option']//span[normalize-space(text())='inputForm']"
    )
    CHOOSE_FORM_SELECT = "//label[normalize-space(text())='Choose Form']//..//div[@class='choices form-group formio-choices']"
    CREATE_FORM_TYPE_TO_SEARCH_ACTIVE = "//div[@class='choices__list choices__list--dropdown is-active']//input[@placeholder='Type to search']"
    FORM_TYPE_INPUTFORM = "//div[@class='choices__item choices__item--selectable']//span[normalize-space(text())='inputForm']"
    USE_EXISTINGFORM_IFCHECKED = "//span[normalize-space(text())='Use existing form']//..//input[@checked='true']"
    SUBMIT_BTN = "//div//button[@type='submit']"
    BACK_BTN_INPUTFORM_EDITPAGE = "//button[@class='btn btn-primary back-btn']"
    FORM_LIST_ACTIVE_LIST = "//div[@class='choices__list choices__list--dropdown is-active']//div[@class='choices__list']"
    NO_FORM_AVAIALABLE_LIST = "//div[@class='choices__list']//div[normalize-space(text())='No choices to choose from']"
    NO_DATA_FOUND_INPUTFORM = (
        "//table//tfoot//tr//th[normalize-space(text())='No Data Found.']"
    )
    DELETED_SUCCESS_MESSAGE = "//div[@class='alert alert-success' and normalize-space(text())='Success! Record(s) are pushed to queue will be processed in some time.']//button[@data-dismiss='alert']//span"
    ACTIVE_TYPE_TO_SEARCH = "//div[@class='choices__list choices__list--dropdown is-active']//input[@placeholder='Type to search']"


class ApprovalInputFormEntryPageLocators:
    APP_SUBMIT_BUTTON = "//button[normalize-space(text())='Submit']"
    APP_SAVE_BUTTON = "//button[normalize-space(text())='SAVE']"
    APP_APPROVE_BUTTON = "//button[normalize-space(text())='Approve']"
    APP_REJECT_BUTTON = "//button[normalize-space(text())='Revert']"
    TAB_NEW_ENTRIES = "//span[normalize-space(text())='New Entries']"
    TAB_APPROVED = "//span[normalize-space(text())='Approved']"
    TAB_REVERTED = "//span[normalize-space(text())='Reverted']"
    TAB_CANCELLED = "//span[normalize-space(text())='Cancelled']"
    TAB_VIEW_ALL = "//span[normalize-space(text())='View All']"
    TAB_DRAFT = "//span[normalize-space(text())='Draft']"


class UserGroupPageLocators:
    USERGROUP_MENU = "//div[@class='sidebar']//div[@class='menus']//div//a//div[normalize-space(text())='User Groups']"
    USERGROUP_TABLE = "//table[@aria-describedby='userGroup']"
    ADD_USERGROUP = "//button[normalize-space(text())='Add Group']"
    USERGROUP_SEARCH = "//button[normalize-space(text())='Search']"
    USERGROUP_INPUT_SEARCHFIELD = "//div//input[@placeholder='User Group Name Filter']"
    USERGROUP_BREADCRUMB = "(//div[@class='container']//div)[2]//span"
    USERGROUP_NAME = "//app-input-view-edit[@label='Name']"
    USERGROUP_INPUT_NAME = "//input[@name='name']"
    USERGROUP_USERSASSOCIATED_SEARCHBTN = "//h6[normalize-space(text())='Users Associated']//..//div//button[normalize-space(text()='Search')]"
    USERGROUP_PROJECTS_SEARCHBTN = "//h6[normalize-space(text())='Projects']//..//div//button[normalize-space(text()='Search')]"
    USERGROUP_USERSASSOCIATED_SEARCH_INPUT = (
        "//h6[normalize-space(text())='Users Associated']//..//div//input"
    )
    USERGROUP_PROJECTS_SEARCHBTN_INPUT = (
        "//h6[normalize-space(text())='Projects']//..//div//input"
    )
    USERGROUP_USERS_ASSOCIATED_LIST_ADDBTN = (
        "//app-chip-card[@title='Users Associated']//button//i[@class='fa fa-plus']"
    )
    USERGROUP_PROJECTS_LIST_ADDBTN = "//app-chip-card//h6[normalize-space(text())='Projects']//..//..//div[@class='card-body']//button//i[@class='fa fa-plus']"
    USERGROUP_USERS_ASSOCIATED_LIST = (
        "//app-chip-card[@title='Users Associated']//ng-select//div[@role='combobox']"
    )
    USERGROUP_PROJECTS_LIST = "//h6[normalize-space(text())='Projects']//..//..//div[@class='card-body']//ng-select//div[@role='combobox']"


class FieldEntryPageLocators:
    TEST = ""


class calendarLocators:
    CALENDAR_MENU = "//div[@class='sidebar']//div[@class='menus']//div//a//div[normalize-space(text())='Calendar']"
    CALENDAR_BREADCRUMB = "(//div[@class='container']//div)[2]//span"
    ADD_CALENDAR = "//button[normalize-space(text())='Add Calendar']"
    CALENDAR_NAME = "//input[@name='name']"
    CALENDAR_SAVE_BUTTON = "//button[@type='submit']"
    STARTDATE_FIELD = "//input[@name='startMonth']"
    ENDDATE_FIELD = "//input[@name='endMonth']"
    ASSERT_CALENDAR_NAME = "//td[normalize-space(text())='CalendarQKfkTjqv']"
    ASSERT_STARTDATE_FIELD = "//td[normalize-space(text())='CalendarQKfkTjqv']"
    ASSERT_ENDDATE_FIELD = "//td[normalize-space(text())='CalendarQKfkTjqv']"


class RolesClaimsPageLocators:
    ROLESCLAIMS_MENU = "//div[@class='sidebar']//div[@class='menus']//div//a//div[normalize-space(text())='Roles & Claims']"
    ROLESCLAIMS_BREADCRUMB = "(//div[@class='container']//div)[2]//span"
    ROLESCLAIMS_CREATE_ROLE = (
        "//div[@id='role-claim-header']/div/button[@id='CreateRoleBtn']"
    )
    ROLESCLAIMS_ROLENAME = "//div[@ref='element']/input[@placeholder='Enter Role']"
    ROLESCLAIMS_DESCRIPTION = "//div[@ref='element']/input[@placeholder='Description']"
    ROLESCLAIMS_SUBMITBUTTON = "//div[@ref='component']/button[@type='submit']"
    ROLESCLAIMS_SUBMITREFRESHICON = (
        "//i[@class='fa fa-refresh fa-spin button-icon-right']"
    )
    ROLESCLAIMS_EDITPAGE_CANCEL = (
        "//h4[normalize-space(text())='Update Role']//..//button[@class='close']//span"
    )


class ResponseDelete:
    deleteBtnResponsePage = "//button[normalize-space(text())='Delete']"
    confirmationDeleteBtn = "//h5[normalize-space(text())='Confirmation']//..//..//..//div[@class='modal-footer']//button[normalize-space(text())='Delete']"
    cancelCancelBtn = "//h5[normalize-space(text())='Confirmation']//..//..//..//div[@class='modal-footer']//button[normalize-space(text())='Cancel']"
    singleDeleteBtn = "//button//i[@class='fa fa-trash']"
    singleDeleteBtnFirstIndex = "(//button//i[@class='fa fa-trash'])[1]"
    singleDeleteConfirmation = "//button[@type='button'][normalize-space()='Delete']"
    singleDeleteSuccess = "//div[@class='alert alert-success' and normalize-space(text())='Success! Record deleted successfully.']//button//span[@aria-hidden='true']"


class DashboardListPagLocator:
    dashboardSearchField = "//input[@placeholder='Search Dashboard']"


class ExternalApiLocators:
    EXTERNALAPI_TAB = "//div[@class='collapse navbar-collapse']//ul//li//a[normalize-space(text())='External API']"
    EXTERNALAPI_TAB_ACTIVE = "//div[@class='collapse navbar-collapse']//ul//li//a[@class='nav-link active' and normalize-space(text())='External API']"
    EXTERNALAPI_TYPE_FIELD = (
        "//div[@class='d-flex justify-content-end']//ng-select[@name='externalApiType']"
    )
    EXTERNALAPI_TYPE_TOKENAPI = "//div[@class='d-flex justify-content-end']//ng-select/ng-dropdown-panel//div//div//span[normalize-space(text())='Token Api']"
    EXTERNALAPI_TYPE_INPUTFORMAPI = "//div[@class='d-flex justify-content-end']//ng-select/ng-dropdown-panel//div//div//span[normalize-space(text())='Input Form Api']"
    EXTERNALAPI_SEARCHFORM_NAME = "//div[@class='search']//input"
    EXTERNALAPI_SEARCH_BUTTON = "//div[@class='search']//I[@class='fa fa-search']"
    EXTERNALAPI_APPLOADER_HIDDEN = "//app-loader//div[@class='hidden']"
    EXTERNALAPI_SHIMMER_LASTRUN_AND_STATUS = (
        "//tbody//tr//td//span[@class='shimmer d-block']"
    )
    EXTERNALAPI_FORM_NAME_LIST = (
        "//table[@aria-describedby='externalApi']//tbody//tr//td//a"
    )
    EXTERNALAPI_SUCCESSMESSAGE_CANCEL_BTN = "//div[@class='toast-wrap']//div[normalize-space(text())='Success! Triggered ExternalApi successfully']//button//span[@aria-hidden='true']"
    EXTERNALAPI_INPUTFORM_NODATAFOUND = (
        "//tfoot//tr//th[normalize-space(text())='No Data Found.']"
    )
    EXTERNALAPI_INPUTFORM_TBODY = (
        "//table[@aria-describedby='Form Response table']//tbody"
    )


class Shimmer:
    NON_APPROVAL_SHIMMER = "(//table[@aria-describedby='Form Response table']//tbody//tr[@class='shimmer-row'])[1]"


class DashboardLoginComponent:
    Pledges_7_images = "//div[@class='content']//img[@alt='7 Pledges by DMK']"
    Pledges_7_images_close_btn = "//a[@class='close-modal icon-close']"


class DashboardComponents:
    ValueInCard_ForCostColumn = "(//div[@class='card-body']//p[normalize-space(text())='Cost']//..//p[@class='card-value']//span[text()])[1]"


class DashboardListPage:
    SearchField_DashboardList = "//div//input[@placeholder='Search Dashboard']"
    dashboard_Grid_Icon = "//button//i[@class='icon-grid icon']"
    dashboard_Grid_Icon_active = "//button[@class='active']//i[@class='icon-grid icon']"
    dashboard_Grid_List = "//button//i[@class='icon-list icon']"
    dashboard_Grid_List_active = "//button[@class='active']//i[@class='icon-list icon']"
    dashboard_Folder_List = "//button//i[@class='icon-folder icon']"
    dashboard_Folder_List_Active = (
        "//button[@class='active']//i[@class='icon-folder icon']"
    )

    dashboard_ByName = "//app-dashboard-icon//div/div[@class='name' and normalize-space(text())='Automation Testing']"
    dashboard_title_Value = "//section//div[text()]"
    dashboard_Footer_Value = (
        "//footer//h3[normalize-space(text())='Automation Testing']"
    )
    dashboard_forms = "//ul[@class='forms']//li"


class Dashboard_MenuBar_Component:
    MenuBar = "//my-menubar"


class DashboardPages:
    Active_DashboardPages = "//ul//li//button[contains(@class,'active')]"


class DataLoading:
    DataLoading_Loader_In_DashboardPage = (
        "//div[@class='loader-toast']//div[normalize-space()='Data Loading...']"
    )
