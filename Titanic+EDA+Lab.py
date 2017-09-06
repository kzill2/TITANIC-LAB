
# coding: utf-8

# In[1]:

import pandas as pd
get_ipython().magic('pylab inline')


# In[2]:

df = pd.read_csv('train.csv')


# ## TITANIC EDAs

# ### PassengerId EDA

# #### PassengerId is categorical as it labels the Titanic passengers. 

# In[3]:

df.PassengerId.value_counts()


# #### There are no missing values of PassengerId.

# In[4]:

df[df.PassengerId.isnull()]


# #### PassengerId Histogram

# In[5]:

df.PassengerId.value_counts().plot(kind='bar')


# ### Survived EDA

# #### Survived is a categorical variable. 

# In[6]:

df.Survived.value_counts()


# #### There are no missing values of Survived.

# In[8]:

df[df.Survived.isnull()]


# #### Survived Histogram

# In[9]:

df.Survived.value_counts().plot(kind='barh')


# ### Pclass EDA

# #### Pclass is a categorical variable. 

# In[10]:

df.Pclass.value_counts()


# #### There are no missing values of Pclass.

# In[11]:

df[df.Pclass.isnull()]


# #### Pclass Histogram

# In[12]:

df.Pclass.value_counts().plot(kind='bar')


# ### Sex EDA

# #### Sex is a categorical variable.

# In[13]:

df.Sex.value_counts()


# #### There are no missing values of Sex.

# In[14]:

df[df.Sex.isnull()]


# #### Sex Histogram

# In[15]:

df.Sex.value_counts().plot(kind='bar')


# ### Age EDA

# #### Age is a continuous variable.

# In[16]:

df.Age.value_counts()


# #### There are 177 missing values of Age. 

# In[17]:

df[df.Age.isnull()]


# #### Min, Max, Average and Standard Deviation for Age

# In[18]:

df.Age.min()


# In[19]:

df.Age.max()


# In[20]:

df.Age.mean()


# In[21]:

df.Age.std()


# #### Age Histogram

# In[22]:

df.Age.hist()


# ### SibSp EDA 

# #### SibSp is a continuous variable.

# In[23]:

df.SibSp.value_counts()


# #### There are no missing values of SibSp.

# In[24]:

df[df.SibSp.isnull()]


# #### Min, Max, Average and Standard Deviation for SibSp

# In[25]:

df.SibSp.min()


# In[26]:

df.SibSp.max()


# In[27]:

df.SibSp.mean()


# In[28]:

df.SibSp.std()


# #### SibSp Histogram

# In[31]:

df.SibSp.hist(bins=8)


# ### Parch EDA

# #### Parch is a continuous variable. 

# In[32]:

df.Parch.value_counts()


# #### There are no missing values of Parch.

# In[33]:

df[df.Parch.isnull()]


# #### Max, Min, Average and Standard Deviation for Parch

# In[34]:

df.Parch.min()


# In[35]:

df.Parch.max()


# In[36]:

df.Parch.mean()


# In[37]:

df.Parch.std()


# #### Parch Histogram

# In[38]:

df.Parch.hist(bins=6)


# ### Ticket EDA

# #### Ticket is a Categorical variable.

# In[39]:

df.Ticket.value_counts()


# #### There are no missing values of Ticket.

# In[40]:

df[df.Ticket.isnull()]


# In[41]:

df.Ticket.value_counts().plot(kind='bar')


# ### Fare EDA

# #### Fare is a continuous variable. 

# In[42]:

df.Fare.value_counts()


# #### There are no missing values of Fare.

# In[44]:

df[df.Fare.isnull()]


# #### Min, Max, Average and Standard Deviation of Fare

# In[45]:

df.Fare.min()


# In[46]:

df.Fare.max()


# In[47]:

df.Fare.mean()


# In[48]:

df.Fare.std()


# #### Fare Histogram

# In[53]:

df.Fare.hist()


# ### Cabin EDA

# #### Cabin is a categorical variable.

# In[54]:

df.Cabin.value_counts()


# #### There are 687 missing values of Cabin.

# In[55]:

df[df.Cabin.isnull()]


# #### Cabin Histogram

# In[56]:

df.Cabin.value_counts().plot(kind='bar')


# ### Embarked EDA

# #### Embarked is a categorical variable.

# In[57]:

df.Embarked.value_counts()


# #### There are two missing values of Embarked.

# In[58]:

df[df.Embarked.isnull()]


# #### Embarked Histrogram

# In[59]:

df.Embarked.value_counts().plot(kind='bar')


# ## CHECK FOR CONTINUOUS VARIABLES

# #### Note: PassengerId, Survived and Pclass are not continuous variables. Although they are numerical, their purpose is to label items. Thus, they cannot be continuous variables. 

# In[60]:

df.describe()

