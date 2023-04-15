from django.contrib import admin

# Register your models here.

from skills_TaggingField.models import (
                        #RELATED DATABASE
                        BehaviouralChallange,
                        SolvingApproachGeneral,
                        SolvingApproachSpecific,
                        ProjectExperience,
                        CodingQuality,
                        DataStructuresAndAlgorithms,
                        DataBaseSQL,
                        LanguagesBackend,
                        FrameworkBackend,
                        FrameworkFrontend,
                        Ides,
                        TextEditors,
                        CloudComputing,
                        WebDevelopment,
                        Containers,
                        Teamwork,
                        JobPerformence,
                        LearningCapacity,
                        FocusStyle,
                        TimeManagement,
                        CommunicationSkills,
                        Leadership,
                        Languages,
                        Education,
                        ComputerScienceCourses,
                        InvolvedSDLC,
                        SdlcPhases,

                        #COMPANY
                        ProvidedBenefits,
                        ProvidedVacationTypes,
                        ProvidedInsuranceTypes,
                        ProductsAndervices,
                        )


#RELATED DATABASE
admin.site.register(BehaviouralChallange)
admin.site.register(SolvingApproachGeneral)
admin.site.register(SolvingApproachSpecific)
admin.site.register(ProjectExperience)
admin.site.register(CodingQuality)
admin.site.register(DataStructuresAndAlgorithms)
admin.site.register(DataBaseSQL)
admin.site.register(LanguagesBackend)
admin.site.register(FrameworkBackend)
admin.site.register(FrameworkFrontend)
admin.site.register(Ides)
admin.site.register(TextEditors)
admin.site.register(CloudComputing)
admin.site.register(WebDevelopment)
admin.site.register(Containers)
admin.site.register(Teamwork)
admin.site.register(JobPerformence)
admin.site.register(LearningCapacity)
admin.site.register(FocusStyle)
admin.site.register(TimeManagement)
admin.site.register(CommunicationSkills)
admin.site.register(Leadership)
admin.site.register(Languages)
admin.site.register(Education)
admin.site.register(ComputerScienceCourses)
admin.site.register(InvolvedSDLC)
admin.site.register(SdlcPhases)




#COMPANY
admin.site.register(ProvidedBenefits)
admin.site.register(ProvidedVacationTypes)
admin.site.register(ProvidedInsuranceTypes)
admin.site.register(ProductsAndervices)
